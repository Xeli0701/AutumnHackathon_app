from onmt.translate.translator import build_translator
import onmt.opts as opts
from onmt.utils.parse import ArgumentParser
import MeCab


class GenerativeSystem:
    def __init__(self):
        # おまじない
        parser = ArgumentParser()
        opts.config_opts(parser)
        opts.translate_opts(parser)
        self.opt = parser.parse_args(args = ["-model","../models/dlg_model_step_150000.pt","-src","None","-replace_unk","--beam_size","10","--min_length","7","--block_ngram_repeat","2"])
        ArgumentParser.validate_translate_opts(self.opt)
        self.translator = build_translator(self.opt, report_score=True)

        # 単語分割用にMeCabを使用
        self.mecab = MeCab.Tagger("-Owakati")
        self.mecab.parse("")

    def initial_message(self, input):
        return {'utt': 'こんにちは。対話を始めましょう。', 'end': False}

    def reply(self, input):
        # 単語を分割
        src = [self.mecab.parse(input)]
        # OpenNMTで応答を生成
        scores, predictions = self.translator.translate(
            src=src,
            tgt=None,
            src_dir=self.opt.src_dir,
            batch_size=self.opt.batch_size,
            attn_debug=False
        )
        # OpenNMTの出力も単語に分割されているので，半角スペースを削除
        reply = predictions[0][0].replace(" ", "")
        return reply

if __name__ == '__main__':
    system = GenerativeSystem()
    reply = system.reply('それめっちゃ面白くない！？')
    print(reply)
    