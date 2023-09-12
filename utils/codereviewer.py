# This file contains utilities for working with the CodeReviewer model.
import torch

MAX_SOURCE_LENGTH = 512


def process_tokenizer(tokenizer):
    """
    Add special tokens to tokenizer.
    :param tokenizer: Transformers tokenizer.
    :return: Return the tokenizer with special tokens.
    """
    tokenizer.special_dict = {
        f"<e{i}>": tokenizer.get_vocab()[f"<e{i}>"] for i in range(99, -1, -1)
    }
    tokenizer.mask_id = tokenizer.get_vocab()["<mask>"]
    tokenizer.bos_id = tokenizer.get_vocab()["<s>"]
    tokenizer.pad_id = tokenizer.get_vocab()["<pad>"]
    tokenizer.eos_id = tokenizer.get_vocab()["</s>"]
    tokenizer.msg_id = tokenizer.get_vocab()["<msg>"]
    tokenizer.keep_id = tokenizer.get_vocab()["<keep>"]
    tokenizer.add_id = tokenizer.get_vocab()["<add>"]
    tokenizer.del_id = tokenizer.get_vocab()["<del>"]
    tokenizer.start_id = tokenizer.get_vocab()["<start>"]
    tokenizer.end_id = tokenizer.get_vocab()["<end>"]

    return tokenizer


def pad_assert(tokenizer, source_ids):
    """
    Pad the source_ids to MAX_SOURCE_LENGTH.
    :param tokenizer: Transformers tokenizer.
    :param source_ids: Source ids.
    :return: Return the padded source ids.
    """
    source_ids = source_ids[: MAX_SOURCE_LENGTH - 2]
    source_ids = [tokenizer.bos_id] + source_ids + [tokenizer.eos_id]
    pad_len = MAX_SOURCE_LENGTH - len(source_ids)
    source_ids += [tokenizer.pad_id] * pad_len
    assert len(source_ids) == MAX_SOURCE_LENGTH, "Not equal length."
    return source_ids


def encode_diff(tokenizer, diff, msg, source):
    difflines = diff.split("\n")[1:]  # remove start @@
    difflines = [line for line in difflines if len(line.strip()) > 0]
    map_dic = {"-": 0, "+": 1, " ": 2}

    def f(s):
        if s in map_dic:
            return map_dic[s]
        else:
            return 2

    labels = [f(line[0]) for line in difflines]
    difflines = [line[1:].strip() for line in difflines]
    inputstr = "<s>" + source + "</s>"
    inputstr += "<msg>" + msg
    for label, line in zip(labels, difflines):
        if label == 1:
            inputstr += "<add>" + line
        elif label == 0:
            inputstr += "<del>" + line
        else:
            inputstr += "<keep>" + line
    source_ids = tokenizer.encode(
        inputstr, max_length=MAX_SOURCE_LENGTH, truncation=True
    )[1:-1]
    source_ids = pad_assert(tokenizer, source_ids)
    return source_ids
