#!/usr/bin/env python3
"""
Fish Speech Colab Example Script

This script demonstrates how to use Fish Speech programmatically in Google Colab
for batch processing or custom applications.

Usage:
    python colab_example.py
"""

import os
import torch
import numpy as np
from pathlib import Path
import pyrootutils

# Setup root path
pyrootutils.setup_root(__file__, indicator=".project-root", pythonpath=True)

from fish_speech.inference_engine import TTSInferenceEngine
from fish_speech.models.dac.inference import load_model as load_decoder_model
from fish_speech.models.text2semantic.inference import launch_thread_safe_queue
from fish_speech.utils.schema import ServeTTSRequest, ServeReferenceAudio


def setup_fish_speech():
    """Initialize Fish Speech models and inference engine."""
    print("🐟 Setting up Fish Speech...")
    
    # Configuration
    device = "cuda" if torch.cuda.is_available() else "cpu"
    precision = torch.bfloat16
    compile_model = False  # Disable for Colab compatibility
    
    llama_checkpoint_path = Path("checkpoints/openaudio-s1-mini")
    decoder_checkpoint_path = Path("checkpoints/openaudio-s1-mini/codec.pth")
    decoder_config_name = "modded_dac_vq"
    
    print(f"📱 Device: {device}")
    
    # Load models
    print("🦙 Loading LLAMA model...")
    llama_queue = launch_thread_safe_queue(
        checkpoint_path=llama_checkpoint_path,
        device=device,
        precision=precision,
        compile=compile_model,
    )
    
    print("🎵 Loading VQ-GAN decoder...")
    decoder_model = load_decoder_model(
        config_name=decoder_config_name,
        checkpoint_path=decoder_checkpoint_path,
        device=device,
    )
    
    print("⚙️ Creating inference engine...")
    inference_engine = TTSInferenceEngine(
        llama_queue=llama_queue,
        decoder_model=decoder_model,
        compile=compile_model,
        precision=precision,
    )
    
    print("✅ Fish Speech ready!")
    return inference_engine


def text_to_speech(engine, text, output_path="output.wav"):
    """
    Generate speech from text using random voice.
    
    Args:
        engine: TTSInferenceEngine instance
        text: Text to convert to speech
        output_path: Where to save the audio file
    """
    print(f"🎤 Generating speech: '{text[:50]}...'")
    
    request = ServeTTSRequest(
        text=text,
        references=[],
        reference_id=None,
        max_new_tokens=1024,
        chunk_length=200,
        top_p=0.7,
        repetition_penalty=1.5,
        temperature=0.7,
        format="wav",
    )
    
    # Generate audio
    for result in engine.inference(request):
        if result.code == "final":
            sample_rate, audio_data = result.audio
            
            # Save audio file
            import scipy.io.wavfile as wavfile
            wavfile.write(output_path, sample_rate, audio_data)
            print(f"💾 Audio saved to: {output_path}")
            return output_path
        elif result.code == "error":
            print(f"❌ Error: {result.error}")
            return None
    
    return None


def voice_cloning(engine, text, reference_audio_path, reference_text, output_path="cloned_output.wav"):
    """
    Generate speech with voice cloning.
    
    Args:
        engine: TTSInferenceEngine instance
        text: Text to convert to speech
        reference_audio_path: Path to reference audio file
        reference_text: Text that matches the reference audio
        output_path: Where to save the audio file
    """
    print(f"🎭 Cloning voice for: '{text[:50]}...'")
    
    # Load reference audio
    with open(reference_audio_path, "rb") as f:
        audio_bytes = f.read()
    
    references = [ServeReferenceAudio(audio=audio_bytes, text=reference_text)]
    
    request = ServeTTSRequest(
        text=text,
        references=references,
        reference_id=None,
        max_new_tokens=1024,
        chunk_length=200,
        top_p=0.7,
        repetition_penalty=1.5,
        temperature=0.7,
        format="wav",
    )
    
    # Generate audio
    for result in engine.inference(request):
        if result.code == "final":
            sample_rate, audio_data = result.audio
            
            # Save audio file
            import scipy.io.wavfile as wavfile
            wavfile.write(output_path, sample_rate, audio_data)
            print(f"💾 Cloned audio saved to: {output_path}")
            return output_path
        elif result.code == "error":
            print(f"❌ Error: {result.error}")
            return None
    
    return None


def batch_generate(engine, text_list, output_dir="outputs"):
    """
    Generate multiple audio files from a list of texts.
    
    Args:
        engine: TTSInferenceEngine instance
        text_list: List of texts to convert
        output_dir: Directory to save audio files
    """
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"📦 Batch generating {len(text_list)} audio files...")
    
    results = []
    for i, text in enumerate(text_list):
        output_path = os.path.join(output_dir, f"output_{i:03d}.wav")
        result = text_to_speech(engine, text, output_path)
        results.append(result)
        print(f"✅ {i+1}/{len(text_list)} completed")
    
    print(f"🎉 Batch generation complete! Files saved in: {output_dir}")
    return results


def main():
    """Main example function."""
    print("🚀 Fish Speech Colab Example")
    print("=" * 40)
    
    # Initialize Fish Speech
    engine = setup_fish_speech()
    
    # Example 1: Basic text-to-speech
    print("\n📝 Example 1: Basic Text-to-Speech")
    text_to_speech(
        engine, 
        "Hello! This is Fish Speech running in Google Colab. It sounds amazing!",
        "example_basic.wav"
    )
    
    # Example 2: Multilingual text
    print("\n🌍 Example 2: Multilingual Text")
    multilingual_text = "Hello! 你好! こんにちは! 안녕하세요! Bonjour! Hola!"
    text_to_speech(engine, multilingual_text, "example_multilingual.wav")
    
    # Example 3: Batch generation
    print("\n📦 Example 3: Batch Generation")
    texts = [
        "The quick brown fox jumps over the lazy dog.",
        "Fish Speech is an amazing text-to-speech system.",
        "Google Colab makes it easy to run AI models in the cloud.",
    ]
    batch_generate(engine, texts, "batch_outputs")
    
    # Example 4: Voice cloning (if reference audio exists)
    reference_audio = "reference.wav"  # You would need to upload this
    if os.path.exists(reference_audio):
        print("\n🎭 Example 4: Voice Cloning")
        voice_cloning(
            engine,
            "This is a cloned voice speaking new text!",
            reference_audio,
            "Original text that matches the reference audio",
            "example_cloned.wav"
        )
    else:
        print("\n🎭 Example 4: Voice Cloning (Skipped - no reference audio)")
        print("Upload a reference.wav file to try voice cloning!")
    
    print("\n🎉 All examples completed!")
    print("Check the generated audio files in your Colab environment.")


if __name__ == "__main__":
    main()
