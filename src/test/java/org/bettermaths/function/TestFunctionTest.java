package org.bettermaths.function;

import org.bettermaths.result.OperationalResult;
import org.bettermaths.result.Result;
import org.bettermaths.result.primary.BooleanResult;
import org.bettermaths.result.primary.DoubleResult;
import org.bettermaths.result.primary.IntegerResult;
import org.bettermaths.token.Tokenizer;
import org.bettermaths.token.function.Function;
import org.bettermaths.token.function.Params;
import org.bettermaths.token.function.argument.Arguments;
import org.bettermaths.token.function.argument.RangeArgument;
import org.bettermaths.token.symbol.delimiter.Parentheses;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class TestFunctionTest {

    @Test
    void test() {
        var tokenizer = new Tokenizer();
        tokenizer.register(new TestFunction());

        tokenizer.evaluate("test(0,true,2,true,4,true,6,true,8,true)");
    }

    private static class TestFunction extends Function {

        public TestFunction() {
            super("test", new Parentheses(), new Arguments(
                    new RangeArgument<>(OperationalResult.class, 0, 10, 2),
                    new RangeArgument<>(BooleanResult.class, 1, 10, 2)
            ));
        }

        @Override
        public Result<?> onExecute(Params params) {
            assertEquals(10, params.values().size());
            assertEquals(5, params.values(OperationalResult.class).size());
            assertEquals(5, params.values(BooleanResult.class).size());

            assertArrayEquals(new Result[] {
                    new IntegerResult(4), new IntegerResult(6)
            }, params.values(4, 7, 2).toArray());
            assertArrayEquals(new Result[] {
                    new IntegerResult(4), new IntegerResult(6), new IntegerResult(8)
            }, params.values(OperationalResult.class, 4, 9).toArray());

            assertArrayEquals(new Result[] {
                    BooleanResult.TRUE, BooleanResult.TRUE
            }, params.values(BooleanResult.class, 4, 8).toArray());

            assertArrayEquals(new Result[0], params.values(DoubleResult.class).toArray());

            return BooleanResult.TRUE;
        }
    }
}
