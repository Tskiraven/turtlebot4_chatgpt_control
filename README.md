first
need to export OPENAI_API_KEY="OpenAI- KEY"
Second
source install/setup.bash
Third
ros2 run turtlebot4_chatgpt_control terminal_control

---------------------------------------------------------
# 🤖 turtlebot4_chatgpt_control

使用 ChatGPT 控制 TurtleBot4，讓你透過「中文自然語言」指令如：

- 往前走一公尺
- 右轉 90 度
- 左轉 45 度

自動轉換為程式控制指令，並立即讓機器人執行！

---

## 📦 安裝步驟

### 1️⃣ 複製專案到 ROS2 Workspace

```bash
cd ~/ros2_ws/src
git clone https://github.com/你的帳號/turtlebot4_chatgpt_control.git
```

### 2️⃣ 安裝 Python 套件
```bash
pip install openai
```

3️⃣ 設定 OpenAI API Key
```bash
export OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```
建議加進 ~/.bashrc：
```bash
echo 'export OPENAI_API_KEY="sk-..."' >> ~/.bashrc
```

4️⃣ 編譯套件
```bash
cd ~/ros2_ws
colcon build --packages-select turtlebot4_chatgpt_control
source install/setup.bash
```
🚀 執行方式
```bash
ros2 run turtlebot4_chatgpt_control terminal_control
```
會出現：
```bash
==== 請輸入自然語言控制 TurtleBot4 ====
>>> 往前走一公尺
ChatGPT 轉換指令：move_forward(1.0)
```
