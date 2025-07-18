import gradio as gr


def greet(name):
    return "Hello " + name + "!"

# Blocksでレイアウトを構築
with gr.Blocks() as demo:
    # 入力コンポーネント
    name = gr.Textbox(label="Name")
    # 出力コンポーネント
    output = gr.Textbox(label="Output Box")
    # ボタンコンポーネント
    greet_btn = gr.Button("Greet")
    # イベントリスナー: ボタンクリック時にgreet関数を実行
    greet_btn.click(fn=greet, inputs=name, outputs=output, api_name="greet")

demo.launch()
