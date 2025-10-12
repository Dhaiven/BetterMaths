package org.bettermaths.token.symbol;

import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class WordManager {
    private static final Set<String> GLOBAL_WORDS = new HashSet<>(List.of("true", "false"));

    public static boolean isWord(String s) {
        return GLOBAL_WORDS.contains(s);
    }

    public static void addWord(String word) {
        GLOBAL_WORDS.add(word);
    }

    public static Set<String> allWords() {
        return Collections.unmodifiableSet(GLOBAL_WORDS);
    }
}

