import pytest
from huffman import HuffmanCode

test_data = [
    ('BACABA', 5.33),
    ('abbcccddddeeeeeffffff', 3.29),
    ('Compression algorithms are usually judged by the compression ratio, which is defined as the ratio between the compressed size and the original size.', 1.9),
    ('The quick brown fox jumps over the lazy dog', 1.77),
]

@pytest.mark.parametrize("test_input,expected_ratio", test_data)
def test_huffman_coding(test_input, expected_ratio):
    huffman = HuffmanCode()
    tree, codes, encoded = huffman.encode(test_input)
    compression_ratio = (8 * len(test_input)) / len(encoded)
    assert round(compression_ratio, 2) == expected_ratio
    assert huffman.decode(codes, encoded) == test_input
    assert huffman.decode_by_tree(tree, encoded) == test_input
    manual_encoded = ''.join(codes[char] for char in test_input)
    assert encoded == manual_encoded