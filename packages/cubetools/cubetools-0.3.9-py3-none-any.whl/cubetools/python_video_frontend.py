import random
import gradio as gr
from serviceboot.serviceboot import serviceboot_client, gen_api_docs


class PythonVideoFrontend(object):

    # 在__init__中定义Python前端界面
    def __init__(self,
                 model_name_cn,
                 model_name_en=None,
                 local_image=True,
                 streaming_video=True,
                 show_image_results=False,
                 results2text=lambda x: x,
                 image_examples=[],
                 video_examples=[],
                 readme='README.md'
                 ):
        self.results2text = results2text if results2text else lambda x: x
        title = f'CubeAI应用示范——{model_name_cn}'
        if model_name_en:
            url_model_zoo = 'https://openi.pcl.ac.cn/cubeai-model-zoo/cubeai-model-zoo'
            url_model = f'https://openi.pcl.ac.cn/cubeai-model-zoo/{model_name_en}'
            description = f'源自 [《CubeAI模型示范库》]({url_model_zoo}) 项目： [{model_name_cn}]({url_model})'

        with gr.Blocks(title=title) as self.demo:
            gr.Markdown('<br/>')
            gr.Markdown(f'# <center>{title}</center>')
            gr.Markdown('<br/>')
            if model_name_en:
                gr.Markdown(description)
                gr.Markdown('<br/>')

            if local_image:
                with gr.Tab("本地图片"):
                    with gr.Row():
                        img1 = gr.Image(show_label=False).style(height='auto')
                        img2 = gr.Image(show_label=False)
                    btn_predict = gr.Button(value='预测')
                    image_results = gr.Textbox(label='预测结果：', visible=show_image_results)
                    self.image_error = gr.Textbox(label='出错了：', visible=False)
                    btn_predict.click(self.predict,
                                     inputs=[img1], outputs=[img2, image_results, self.image_error, self.image_error],
                                     preprocess=False, postprocess=False)
                    examples = [[example] for example in image_examples]
                    if examples:
                        gr.Examples(label='示例', examples=examples, inputs=[img1])

            if streaming_video:
                with gr.Tab("云流媒体"):
                    playing = gr.Number(visible=False, value=0)
                    played = gr.Number(visible=False, value=0)  # 用于在一帧图像播放结束后触发一事件，继续获取下一帧
                    self.url = gr.Textbox(label='流媒体URL', value='rtsp://localhost:8554/stream')
                    self.btn_play = gr.Button(value='播放')
                    self.btn_stop = gr.Button(value='停止', visible=False)
                    img = gr.Image(show_label=False).style(height='auto')
                    self.video_error = gr.Textbox(label='出错了：', visible=False, interactive=False)

                    self.btn_play.click(self.play_video,
                                        inputs=[self.url],
                                        outputs=[img, playing, played, self.video_error, self.video_error, self.url, self.btn_play, self.btn_stop],
                                        show_progress=True, preprocess=False, postprocess=False)
                    self.btn_stop.click(self.stop_video,
                                        outputs=[playing, self.url, self.btn_play, self.btn_stop],
                                        show_progress=False)
                    played.change(self.on_played,
                                  inputs=[playing, self.url],
                                  outputs=[img, played, self.video_error, self.video_error],
                                  show_progress=False, preprocess=False, postprocess=False)
                    self.video_error.change(self.on_error,
                                            inputs=[self.video_error],
                                            outputs=[playing, self.url, self.btn_play, self.btn_stop],
                                            show_progress=False, preprocess=False, postprocess=False)

                    examples = [['rtsp://localhost:8554/stream'], ['rtmp://localhost/stream/live']]
                    for example in video_examples:
                        examples.append([example])
                    gr.Examples(label='URL示例', examples=examples, inputs=[self.url])

            gr.Markdown('<br/>')
            args = []
            if local_image:
                args.append(self.predict)
            if streaming_video:
                args.append(self.predict_video)
            api_text = gen_api_docs(*args)
            btn_show_api = gr.Button(value='显示API文档')
            btn_hide_api = gr.Button(value='隐藏API文档', visible=False)
            api_docs = gr.Markdown(api_text, visible=False)
            btn_show_api.click(lambda: (btn_show_api.update(visible=False), btn_hide_api.update(visible=True), api_docs.update(visible=True)),
                               outputs=[btn_show_api, btn_hide_api, api_docs])
            btn_hide_api.click(lambda: (btn_show_api.update(visible=True), btn_hide_api.update(visible=False), api_docs.update(visible=False)),
                               outputs=[btn_show_api, btn_hide_api, api_docs])

            gr.Markdown('<br/>')
            if readme:
                gr.Markdown(open(readme).read())

    # 在launch方法中启动Python前端服务，必须存在
    def launch(self, **kwargs):
        self.demo.launch(**kwargs)

    def predict(self, img):
        result = serviceboot_client('predict', img=img)
        if result['status'] == 'ok':
            results, img = result['value']
            return img, self.results2text(results), '', self.image_error.update(visible=False)
        return None, '', result['value'], self.image_error.update(visible=True)

    def predict_video(self, url):
        return serviceboot_client('predict_video', url=url)['value']

    def play_video(self, url):
        img_or_err = self.predict_video(url)
        if img_or_err.startswith('data:image'):
            return img_or_err, 1, random.random(), '', \
                   self.video_error.update(visible=False), \
                   self.url.update(interactive=False), \
                   self.btn_play.update(visible=False), \
                   self.btn_stop.update(visible=True)
        return None, 0, 0, img_or_err, \
               self.video_error.update(visible=True), \
               self.url.update(interactive=True), \
               self.btn_play.update(visible=True), \
               self.btn_stop.update(visible=False)

    def on_played(self, playing, url):
        if playing:
            img_or_err = self.predict_video(url)
            if img_or_err.startswith('data:image'):
                return img_or_err, random.random(), '', self.video_error.update(visible=False)
            return None, 0, img_or_err, self.video_error.update(visible=True)
        return None  # 这里会抛出异常，因为正常返回值应该是多个。为了在按停止按钮后仍保留视频画面，故意这样写的。

    def stop_video(self):
        return 0, self.url.update(interactive=True), self.btn_play.update(visible=True), self.btn_stop.update(visible=False)

    def on_error(self, error):
        if error:
            return 0, self.url.update(interactive=True), self.btn_play.update(visible=True), self.btn_stop.update(visible=False)
        return None  # 这里会抛出异常，因为正常返回值应该是多个。为了在主动清空error时不改变状态，故意这样写的。
