@echo off
echo 正在打包 AutoTypingTool...
pyinstaller --noconfirm --log-level=WARN --onefile --windowed --icon=icon.ico AutoTypingTool.py
echo ✅ 打包完成！EXE 文件位于 dist/AutoTypingTool.exe
pause