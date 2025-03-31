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
