from fastmcp import FastMCP

mcp = FastMCP(
    name="My MCP Server",
    instructions="这是一个欢迎MCP服务器，你可以使用它来调用greet工具。用户输入的名字，服务器将返回一个欢迎消息。"
)

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run()
