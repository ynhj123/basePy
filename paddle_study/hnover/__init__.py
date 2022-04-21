import os

import paddlehub as hub


def load_vocab(vocab_file):
    """Loads a vocabulary file into a dictionary."""
    fin = open(vocab_file)
    for num, line in enumerate(fin):
        print(num + ":" + line)


if __name__ == '__main__':
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"
    # load_vocab("C:\\Users\\ynhj\\.paddlehub\\modules\\plato2_en_base\\assets\\vocab.txt")
    module = hub.Module(name="plato2_en_base")
    # 直接产生对话：
    text = "what you want to say"
    response = module.generate([text])
    # 多轮对话
    with module.interactive_mode(max_turn=3):
        your_words = input()
        response = module.generate(your_words)
        print("robot answer: %s" % response)
