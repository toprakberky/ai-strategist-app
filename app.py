import gradio as gr
import requests

# Your DeepInfra API Key
api_key = "yv0wnFGMATMbtFm4J8ErqWbvpuUk3vch"

def create_plan(sektor, hedef_kitle, durum):
    prompt = f"""
    İş Modeli: {sektor}
    Hedef Kitle: {hedef_kitle}
    Mevcut Durum: {durum}

    Kısa bir SWOT analizi ve temel iş planı önerisi oluştur.
    (Türkçe olarak yanıt ver.)
    """

    url = "https://api.deepinfra.com/v1/openai/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "meta-llama/Llama-2-70b-chat-hf",
        "messages": [
            {"role": "system", "content": "Sen bir iş stratejisi uzmanısın."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 600
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        sonuc = response.json()['choices'][0]['message']['content']
        return sonuc
    else:
        return "Bir hata oluştu."

# Gradio Interface
iface = gr.Interface(
    fn=create_plan,
    inputs=[
        gr.Textbox(label="İş fikriniz hangi sektörde?"),
        gr.Textbox(label="Hedef kitleniz kim?"),
        gr.Textbox(label="Şu anki durumunuz veya probleminiz nedir?")
    ],
    outputs="text",
    title="🚀 AI Destekli İş Planı & SWOT Analizi"
)

iface.launch()
