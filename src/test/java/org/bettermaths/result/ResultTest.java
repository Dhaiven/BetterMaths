package org.bettermaths.result;

import org.bettermaths.result.primary.DoubleResult;
import org.bettermaths.result.primary.IntegerResult;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class ResultTest {

    @Test
    void equivalent() {
        ResultManager.get(null); // Juste pour l'init, TODO: vrai manière de init

        assertTrue(new IntegerResult(1).equivalent(new IntegerResult(1)));
        assertTrue(new IntegerResult(1).equivalent(new DoubleResult(1d)));
        assertTrue(new DoubleResult(1d).equivalent(new IntegerResult(1)));
        assertTrue(new DoubleResult(1d).equivalent(new DoubleResult(1d)));

        assertFalse(new DoubleResult(1.2d).equivalent(new IntegerResult(1)));
    }

    @Test
    void compare() {
        ResultManager.get(null); // Juste pour l'init, TODO: vrai manière de init

        assertEquals(0, new IntegerResult(1).compareTo(new IntegerResult(1)));
        assertEquals(0, new IntegerResult(1).compareTo(new DoubleResult(1d)));
        assertEquals(0, new DoubleResult(1d).compareTo(new IntegerResult(1)));
        assertEquals(0, new DoubleResult(1d).compareTo(new DoubleResult(1d)));

        assertEquals(1, new DoubleResult(1.2d).compareTo(new IntegerResult(1)));
        assertEquals(-1, new DoubleResult(1d).compareTo(new DoubleResult(1.2d)));
    }
}
