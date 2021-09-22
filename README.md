# Wearable-shortcut-keyboard

## Purpose

1) 단축키 사용이 편리하게 한다.
2) 키 커맨드가 어렵지 않고 간편하게 사용케 한다.
3) 웨어러블 키보드의 장점을 유지하여 개발한다.

## PC program

> 단축키를 수행할 PC에서 사용하는 프로그램

### Installation

+ git clone https://github.com/CCider21/Wearable-shortcut-keyboard.git
+ pip install pynput
+ Raspberry Pi와 연결된 상태에서 Raspberry Pi 프로그램 먼저 실행 후 PC/main.py 실행

### Usage

<img width="700" alt="Key Mapper1" src="https://user-images.githubusercontent.com/67242042/134286544-fdb3de1d-a089-48f3-bbff-1517308972f5.PNG">

1. Apply 버튼
    + Apply 버튼을 누르면 오른쪽 Sensor-Keybinding 창에 나와있는 센서 입력에 해당하는 mapping 내용이 적용된다.
2. New 버튼
    + 새로운 Preset을 추가한다.
  
3. Delete 버튼
    + 현재 Preset이 삭제된다.
  
4. Preset
    + 원하는 Preset을 선택할 수 있다.
  
5. Rename
    + Rename 옆에 있는 텍스트 박스에 변경할 이름을 적고 Set 버튼을 누르면, Preset의 이름이 변경된다.
  
6. Sensor-Keybinding
    + Wearable shortcut keyboard에서 사용할 수 있는 센서 입력은 총 8개이고, 각각의 센서 입력에 대해 어떠한 단축키를 설정하였는지 보여주는 표이다. 
    + 변경하고자 하는 Keybinding을 더블클릭하면 아래와 같이 키 바인딩 화면이 나온다.
  
    <img width="355" alt="Key Mapper2" src="https://user-images.githubusercontent.com/67242042/134286601-7eb0f040-f516-477a-8411-42584defef61.PNG">   <img width="355" alt="Key Mapper3" src="https://user-images.githubusercontent.com/67242042/134290951-4315e524-dd28-40cd-a643-492cf04f6685.PNG">
    + 키 바인딩 화면으로 바뀐뒤 단축키를 입력하면 화면에 키보드로 입력한 내용이 보여진다. 이때 enter키를 누르면 해당 단축키가 Mapping되고, escape키를 누르면 변경되는 설정 없이 원래 화면으로 되돌아간다.



## Raspberry Pi program

> 웨어러블 키보드 하드웨어 내에서 실행하는 프로그램

### Installation

+ git clone https://github.com/CCider21/Wearable-shortcut-keyboard.git
+ cd Raspberry\ Pi/
+ sudo python3 main.py

### Usage

  <img width="300" alt="WearableShortcutKeyboard1" src="https://user-images.githubusercontent.com/67242042/134286634-8094cb55-2ced-4021-aded-20caf07808f3.PNG">   <img width="330" alt="WearableShortcutKeyboard2" src="https://user-images.githubusercontent.com/67242042/134286645-f0270dc6-af11-40e1-9a9e-03416c11f70e.PNG">

  + 각각의 터치 센서는 짧게 누르는 경우와 길게 누르는 경우 다른 단축키로 동작가능하다.
  + PC 프로그램과 연결된 후 터치센서를 눌러서 맵핑한 단축키를 동작해줄 수 있다.
  
