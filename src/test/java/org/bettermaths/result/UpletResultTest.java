package org.bettermaths.result;

import org.bettermaths.result.custom.UpletResult;
import org.bettermaths.result.custom.VectorResult;
import org.bettermaths.result.primary.IntegerResult;
import org.bettermaths.token.Tokenizer;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class UpletResultTest {

    @Test
    void test() {
        var tokenizer = new Tokenizer();
        assertEquals(new VectorResult(
                new IntegerResult(2), new IntegerResult(1)
        ), tokenizer.evaluate("(2, 1)"));

        assertEquals(new UpletResult(
                new VectorResult(
                        new IntegerResult(1), new IntegerResult(3)
                ),
                new VectorResult(
                    new IntegerResult(2), new IntegerResult(4)
                )
        ), tokenizer.evaluate("((1, 3), (2, 4))"));
    }

    @Test
    void operationOnUpletResult() {
        var tokenizer = new Tokenizer();
        assertEquals(new VectorResult(
                new IntegerResult(5), new IntegerResult(5)
        ), tokenizer.evaluate("(2, 1) + (3, 4)"));
        assertEquals(new VectorResult(
                new IntegerResult(6), new IntegerResult(4)
        ), tokenizer.evaluate("(2, 1) * (3, 4)"));

        assertEquals(new VectorResult(
                new IntegerResult(6), new IntegerResult(3)
        ), tokenizer.evaluate("(2, 1) * 3"));
        assertEquals(new VectorResult(
                new IntegerResult(9), new IntegerResult(18)
        ), tokenizer.evaluate("1.5 * (2, 4) * 3"));
    }
}
