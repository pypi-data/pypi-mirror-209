from .__constants__ import __author__,__copyright__,__description__,__license__,__url__,__version__

def generate_game(game_path:str = "JBQ",record_path:str = None,display:str = "window"):
    import os
    if os.path.exists(game_path):
        return False
    os.mkdir(game_path)
    os.mkdir(os.path.join(game_path,"maps"))
    os.mkdir(os.path.join(game_path,"extensions"))
    with open(os.path.join(game_path,"JBQ.py"),"w",encoding = "utf-8") as wfile:
        wfile.write("from s27a_jbq.game import App\n")
        wfile.write("\n")
        wfile.write(f"""def main():
    app = App(record_path = {repr(record_path)})
    app.run()

if __name__ == "__main__":
    main()
""")
    return True
