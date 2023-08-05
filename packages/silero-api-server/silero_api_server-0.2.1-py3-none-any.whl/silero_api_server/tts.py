# V3
import os, time
import torch
import torch.package
import torchaudio
from hashlib import md5
from loguru import logger

class SileroTtsService:
    """
    Generate TTS wav files using Silero
    """
    def __init__(self, sample_path, sessions_path="sessions") -> None:
        self.sample_text = "The fallowed fallen swindle auspacious goats in portable power stations."
        self.sample_path = sample_path
        self.sessions_path = sessions_path
        # Silero works fine on CPU
        self.device = torch.device('cpu')
        torch.set_num_threads(4)
        torchaudio.set_audio_backend("soundfile")

        # Make sure we  have the model
        self.local_file = 'model.pt'
        if not os.path.isfile(self.local_file):
            logger.warning(f"First run, downloading Silero model. This could take some time...") 
            torch.hub.download_url_to_file('https://models.silero.ai/models/tts/en/v3_en.pt',
                                        self.local_file)  
            logger.info(f"Model download completed.") 


        # Make sure we have the path
        if not os.path.exists('samples'):
            os.mkdir('samples')        
        
        if not os.path.exists(sessions_path):
            os.mkdir(sessions_path)

        self.model = torch.package.PackageImporter(self.local_file).load_pickle("tts_models", "model")
        self.model.to(self.device)

        self.sample_rate = 48000 
        logger.info(f"TTS Service loaded successfully") 

    def generate(self, speaker, text, session=""):
        """
        Generate a TTS wav file and return it. Optional session is provided to save related samples into a folder.
        """
        logger.info(f"Generating text {text} using speaker {speaker}") 
        audio = self.model.save_wav(text=text,speaker=speaker,sample_rate=self.sample_rate)

        # Retain wav files grouped by a session
        if session:
            session_path = os.path.join(self.sessions_path,session)
            if not os.path.exists(session_path):
                os.mkdir(session_path)
            dst = os.path.join(session_path,f"tts_{session}_{int(time.time())}_{speaker}_.wav")
            os.rename(audio,dst)
            audio = dst
        return audio

    def get_speakers(self):
        "List different speakers in model"
        return self.model.speakers

    def generate_samples(self):
        "Remove current samples and generate new ones for all speakers."
        logger.warning("Removing current samples")
        for file in os.listdir(self.sample_path):
            os.remove(f"{self.sample_path}/{file}")

        logger.info("Creating new samples. This should take a minute...")
        for speaker in self.model.speakers: 
            name = f"{speaker}.wav"
            if os.path.exists(name):
                continue
            audio = self.model.save_wav(text=self.sample_text,speaker=speaker,sample_rate=self.sample_rate)
            os.rename(audio, f"{self.sample_path}/{name}")
        logger.info("New samples created")  

    def update_sample_text(self,text: str):
        "Update the text used to generate samples"
        if not text: return
        self.sample_text = text
        logger.info(f"Sample text updated to {self.sample_text}")  

