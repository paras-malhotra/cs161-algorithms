from typing import Optional, Dict, Tuple
from priority_queue import PriorityQueue
from tree_node import Node
from binary_tree import BinaryTree

class HuffmanCode:
    def __init__(self):
        self.freq: Dict[str, int] = {}
        self.code: Dict[str, str] = {}

    def encode(self, s: str) -> Tuple[BinaryTree, Dict[str, str], str]:
        """
        Generate Huffman prefix codes for the given string.

        Args:
            s (str): The input string to be encoded.

        Returns:
            Tuple[BinaryTree, Dict[str, str], str]: A tuple containing the Huffman tree, a dictionary of codes for each character, and the encoded string.
        """
        # Return empty tree and codes for empty string
        if len(s) == 0:
            return BinaryTree(), {}

        # Count frequency of each character in the string
        freq: Dict[str, int] = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        # Create a priority queue to store nodes with their frequencies
        pq = PriorityQueue(lambda v1, v2: v1[0] < v2[0])
        for char, frequency in freq.items():
            pq.insert((frequency, Node(char)))

        # Build Huffman Tree from the bottom up
        while pq.size() > 1:
            freq1, left = pq.extract_min()
            freq2, right = pq.extract_min()
            # A node with key '*' is an internal node
            merged = Node('*', left, right)
            pq.insert((freq1 + freq2, merged))

        # The last node in the priority queue is the root of the Huffman tree
        tree = BinaryTree(pq.extract_min()[1])

        # Helper function to generate Huffman codes
        huffman_codes: Dict[str, str] = {}
        def generate_codes(node: Optional[Node], code: str) -> None:
            if node is None:
                return
            if node.key != '*':  # Leaf node (not internal)
                huffman_codes[node.key] = code
            generate_codes(node.left, code + '0')
            generate_codes(node.right, code + '1')

        # Generate Huffman codes
        generate_codes(tree.root, '')
        encoded = ''.join(huffman_codes[char] for char in s)

        return tree, huffman_codes, encoded

    def decode(self, codes: Dict[str, str], s: str) -> str:
        """
        Decode a Huffman-encoded string.

        Args:
            codes (Dict[str, str]): A dictionary of codes for each character.
            s (str): The Huffman-encoded string.

        Returns:
            str: The decoded string.
        """
        # Return empty string for empty codes
        if len(codes) == 0:
            return ''

        # Invert the codes dictionary
        inverted_codes = {v: k for k, v in codes.items()}

        # Decode the string using the inverted codes dictionary
        decoded = ''
        current = ''
        for bit in s:
            current += bit
            if current in inverted_codes:
                decoded += inverted_codes[current]
                current = ''

        return decoded


    def decode_by_tree(self, tree: BinaryTree, s: str) -> str:
        """
        Decode a Huffman-encoded string.

        Args:
            tree (BinaryTree): The Huffman tree.
            s (str): The Huffman-encoded string.

        Returns:
            str: The decoded string.
        """
        # Return empty string for empty tree
        if tree.root is None:
            return ''

        # Decode the string using the Huffman tree
        decoded = ''
        current = tree.root
        for bit in s:
            if bit == '0':
                current = current.left
            else:
                current = current.right
            if current.key != '*':
                decoded += current.key
                current = tree.root

        return decoded