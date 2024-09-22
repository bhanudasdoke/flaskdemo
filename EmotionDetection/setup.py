from setuptools import setup, find_packages

setup(
    name='EmotionDetection',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'emotion-detection=emotion_detection.emotion_detection:app.run',
        ],
    },
    python_requires='>=3.6',
)
