from dotenv import load_dotenv

from configs.load_configs import load_configs

load_dotenv()
__all__ = ['configs']
configs = load_configs("configs/configs.yaml")
