# 🐟 Fish Speech - Google Colab Edition

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fishaudio/fish-speech/blob/main/fish_speech_colab.ipynb)

## 🚀 Quick Start

1. **Click the "Open in Colab" badge above**
2. **Set GPU Runtime**: `Runtime` → `Change runtime type` → `Hardware accelerator` → `GPU`
3. **Run All Cells**: `Runtime` → `Run all` (or `Ctrl+F9`)
4. **Wait 10-15 minutes** for setup and model loading
5. **Use the Gradio interface** that appears with a public shareable link!

## ✨ Features

- 🎯 **Zero-shot Voice Cloning**: Clone any voice with 10-30 seconds of audio
- 🌍 **Multilingual TTS**: English, Chinese, Japanese, Korean, French, German, Arabic, Spanish
- 🔗 **Public Sharing**: Get a shareable link that works for 72 hours
- 🎨 **Easy Interface**: User-friendly Gradio WebUI
- ⚡ **GPU Optimized**: Runs efficiently on Colab's free GPU

## 📋 Requirements

- **Google Colab Account** (free)
- **GPU Runtime** (T4 or better recommended)
- **Stable Internet** for model downloads (~2-3GB)

## 🎭 How to Use

### Basic Text-to-Speech
1. Enter text in the input field
2. Click "Generate"
3. Listen to the generated speech

### Voice Cloning
1. Upload a reference audio file (10-30 seconds)
2. Enter the text that matches the reference audio
3. Enter your target text (what you want the voice to say)
4. Click "Generate"

## 💡 Tips for Best Results

- **Reference Audio**: Use clear, noise-free recordings
- **Exact Transcription**: Make sure reference text matches the audio exactly
- **Reasonable Length**: Keep target text to reasonable sentence lengths
- **Language Support**: Mix languages freely in your text

## 🔧 Troubleshooting

### Common Issues

**"No GPU available"**
- Go to `Runtime` → `Change runtime type` → Select `GPU`

**"CUDA out of memory"**
- Restart runtime: `Runtime` → `Restart runtime`
- Use shorter text inputs

**"Models not loading"**
- Check internet connection
- Restart runtime and try again

**"Gradio link expired"**
- Re-run the last cell to get a new link

## 📚 What's Included

The Colab notebook automatically:
- ✅ Detects and configures GPU
- ✅ Clones the Fish Speech repository
- ✅ Installs all dependencies
- ✅ Downloads the OpenAudio S1-mini model (~2GB)
- ✅ Loads and optimizes models for inference
- ✅ Launches Gradio WebUI with public sharing
- ✅ Provides comprehensive usage instructions

## 🌐 Sharing Your Interface

The Gradio interface creates a public link like:
```
https://xxxxx.gradio.live
```

This link:
- 📤 Can be shared with anyone
- ⏰ Valid for 72 hours
- 👥 Supports multiple simultaneous users
- 🔒 Automatically expires for security

## ⚖️ License & Responsible Use

Fish Speech is released under CC BY-NC-SA 4.0 License.

**Please use responsibly:**
- 🚫 Don't impersonate others without consent
- 🚫 Don't create misleading content
- 🚫 Don't violate local laws
- ✅ Give credit when sharing generated content

## 🆘 Support

- 📖 **Documentation**: [docs.fish.audio](https://docs.fish.audio)
- 💻 **GitHub**: [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech)
- 🤗 **Hugging Face**: [fishaudio](https://huggingface.co/fishaudio)

---

**Enjoy creating amazing speech with Fish Speech! 🐟🎵**
