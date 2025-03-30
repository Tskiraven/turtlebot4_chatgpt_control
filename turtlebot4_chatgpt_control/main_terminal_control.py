from turtlebot4_chatgpt_control.chatgpt_to_command import language_to_code
import rclpy
from turtlebot4_chatgpt_control.turtlebot_controller import TurtleBotController

def main():
    rclpy.init()
    controller = TurtleBotController()
    print("==== 請輸入自然語言控制 TurtleBot4 ====")

    while True:
        user_input = input(">>> ")
        if user_input.lower() in ['exit', 'quit']:
            break
        try:
            command = language_to_code(user_input)
            print("ChatGPT 轉換指令：", command)
            exec(f"controller.{command}")
        except Exception as e:
            print("發生錯誤：", e)

    controller.destroy_node()
    rclpy.shutdown()
