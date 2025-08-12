from collections import deque


def word_ladder_length(beginWord, endWord, wordList):
    word_set = set(wordList)  # Convert list to set for O(1) lookup

    if endWord not in word_set:
        return 0  # End word not in dictionary, no path

    # Queue for BFS: (current_word, steps)
    queue = deque()
    queue.append((beginWord, 1))

    while queue:
        current_word, steps = queue.popleft()

        # If we reach the end word
        if current_word == endWord:
            return steps

        # Try changing every letter in the word
        for i in range(len(current_word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                # Skip same letter replacement
                if c == current_word[i]:
                    continue

                # Create new word by replacing one character
                new_word = current_word[:i] + c + current_word[i + 1:]

                # If new word is valid and in dictionary
                if new_word in word_set:
                    queue.append((new_word, steps + 1))
                    word_set.remove(new_word)

    return 0  # No valid path found
