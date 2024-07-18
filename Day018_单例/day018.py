class MusicPlayer:
    # 记录第一个被创建对象的引用
    instance = None
    # 记录是否执行过初始化操作
    init_flag = False
    
    def __new__(cls, *args, **kwargs):
        # 如果类属性instance未被初始化
        if cls.instance is None:
            # 调用父类方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)
            
        # 返回类属性保存的对象引用
        return cls.instance
    
    def __init__(self):
        # 判断是否执行过初始化操作       
        if not MusicPlayer.init_flag:
            print("初始化音乐播放器")
            MusicPlayer.init_flag = True

# 创建多个对象           
player1 = MusicPlayer()
print(player1)
player2 = MusicPlayer()
print(player2)