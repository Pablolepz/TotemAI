# TotemAI

### Goals
This project is a simple one:
  #### Software
  - Real time detection of drops in electronic music to play a gif on a screen when a song drops.
  - Secondary Goals:
    - A BPM meter that fluctuates in real time
    - A music visualizer/waveform
    - Temporary gif/screen output if there has been no drop. 
  #### Hardware
  - This program runs on an embedded device that has a microphone and can process the information quickly and in real time. 
    - Expected hardware:
      - Raspberry Pi, arduino, or similar. 
      - A screen that is connected to the embedded device
      - A system integrated into a festival totem including:
        - the battery
        - the microphone
        - the embedded device
        - the monitor/screen
### Setup

- Clone the repo!
- Use the "dev" branch to edit the code, and submit merge requests for new features and bug fixes

#### Requirements

-  Python 3 (3.7.3 minimum)
-  Librosa
-  pyaudio
-  wave
-  PyQT5

#### Resources

- DETECTING DROPS IN ELECTRONIC DANCE MUSIC
  http://www.terasoft.com.tw/conf/ismir2014/proceedings/T026_297_Paper.pdf
