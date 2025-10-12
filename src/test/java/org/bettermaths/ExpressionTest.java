package org.bettermaths;

import org.bettermaths.result.ResultManager;
import org.bettermaths.result.primary.DoubleResult;
import org.bettermaths.result.primary.IntegerResult;
import org.bettermaths.token.Tokenizer;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class ExpressionTest {

    private void equal(String expression, double actual) {
        var tokenizer = new Tokenizer();
        assertEquals(ResultManager.get(actual), tokenizer.evaluate(expression));
    }

    @Test
    void operatorTest() {
        equal("2+2", 4);
        equal("3/7/5", 3d/7d/5d);
        equal("3/5/7", 3d/5d/7d);
        equal("2-2", 0);
        equal("2*2", 4);
        equal("3*2+2", 8);
        equal("(2+2)", 4);
        equal("-7+5", -2);
        equal("-3-5-2", -10);
        equal("5+2-3.5", 3.5);
        equal("3*(2+2)", 12);
        equal("3+2*2", 7);
        equal("(3)", 3);
        equal("2*3*4", 24);
        equal("2/2", 1);
        equal("2.0/4", 0.5);
        equal("8/4/2", 1);
        equal("8/(4/2)", 4);
        equal("(3*5)/5", 3);
        equal("2+2.0/4", 2.5);
        equal("(2+(3+2))", 7);
        equal("((2+(3+2)))", 7);
        equal("-(3+2*5)", -13);
        equal("7/2.0+3.0/4", 17d/4);

        var tokenizer = new Tokenizer();
        assertEquals(new IntegerResult(6), tokenizer.evaluate("2.5+3.5"));
        equal("-3.2", -3.2);
        assertEquals(new IntegerResult(-2), tokenizer.evaluate("- 6 /2 + 1"));

        equal("-4/-2", 2);

        DoubleResult exceptedResult = (DoubleResult) new Tokenizer().evaluate("1/3");
        DoubleResult actualResult = (DoubleResult) ResultManager.get(0.33);
        assertNotEquals(exceptedResult, actualResult);
        assertEquals(exceptedResult.round(), actualResult.round());
    }

    @Test
    void relationTest() {
        var tokeniser = new Tokenizer();
        assertEquals(false, tokeniser.evaluate("true&&false").get());
        assertEquals(false, tokeniser.evaluate("true and false").get());
        assertEquals(true, tokeniser.evaluate("true && true && true").get());
        assertEquals(false, tokeniser.evaluate("true && false and true").get());
        assertEquals(true, tokeniser.evaluate("2=2").get());
        assertEquals(false, tokeniser.evaluate("2+2=2-2").get());
        assertEquals(true, tokeniser.evaluate("true&&false=false&&false").get());
        assertEquals(true, tokeniser.evaluate("true &&true").get());

        assertEquals(false, tokeniser.evaluate("1>2").get());
        assertEquals(true, tokeniser.evaluate("1<=2").get());
        assertEquals(true, tokeniser.evaluate("2>=1").get());

        assertEquals(true, tokeniser.evaluate("2>=1 && 1>0").get());
        assertEquals(true, tokeniser.evaluate("2>=1>0").get());

        assertEquals(false, tokeniser.evaluate("2>=1>2").get());
        assertEquals(false, tokeniser.evaluate("2>=1<0").get());

        assertEquals(true, tokeniser.evaluate("-2<=1>0").get());

        assertEquals(true, tokeniser.evaluate("true||false").get());
        assertEquals(true, tokeniser.evaluate("true or false").get());
        assertEquals(true, tokeniser.evaluate("true || true || true").get());
        assertEquals(false, tokeniser.evaluate("false || false or false").get());

        assertEquals(true, tokeniser.evaluate("truexorfalse").get());
        assertEquals(false, tokeniser.evaluate("true xor true").get());
        assertEquals(true, tokeniser.evaluate("true xor true xor true").get());
        assertEquals(true, tokeniser.evaluate("false xor false xor true").get());
    }

    @Test
    void functionTest() {
        equal("abs(3.54)", 3.54);
        equal("abs(-3)", 3);

        equal("min(-3, 3)", -3);
        equal("min((2*5), 5)", 5);
        equal("min((2*5), 5) + min((2*5), 5)", 10);
        equal("min(2, 3 + 4 * 5)", 2);
    }

    /**@Test
    void complexFunctionTest() {
        Fraction sumResult = Fraction.ZERO;
        StringBuilder sumString = new StringBuilder("sum(");
        //TODO: fix bug when i = 25
        for (int i = 1; i < 20; i++) {
            var added = sumResult.add(Fraction.getFraction(i).invert());
            sumResult = Fraction.getReducedFraction(added.getNumerator(), added.getDenominator());
            sumString.append("1/").append(i).append(",");
        }
        sumString = new StringBuilder(sumString.substring(0, sumString.length() - 1));
        sumString.append(")");

        var tokeniser = new Tokenizer();
        assertEquals(tokeniser.evaluate(sumString.toString()).get(), sumResult);
    }*/

    /**
     * 381 avec expression
     * 607 avec token "final"
     *
     * 606 avec token un peu upgrade
     * 700 avec l'ancienne mais qui prend en compte les espaces
     *
     * Apres changement dans la fonction de mesure du temps:
     * - 345ms: 1er qui marche
     * - 333ms: nouveau marche avec x arguements dans des fonctions
     * - 28_259ms (pour n < 1, sinon trop de temps): avec tout qui marche (je pense c'est car je foreach toute la list pour check
     * si il existe un result)
     */
    /**@Test
    void performanceTest() {
        List<Long> diff = new ArrayList<>();

        for (int nbr = 0; nbr < 100; nbr++) {
            long start = System.nanoTime();
            for (int i = 0; i < 100_000; i++) {
                var expression = new Tokenizer().evaluate("2*2+(8/4)+(-1+2)");
            }
            long end = System.nanoTime();
            diff.add(end - start);
        }

        // Moyenne en ms
        long sum = 0;
        for (long d : diff) sum += d;
        double averageMs = (sum / (double) diff.size()) / 1_000_000;
        System.out.println("Temps moyen : " + averageMs + " ms");
    }*/
    /**
     * 594
     * 606
     * 539
     */

    @Test
    void tryMathParserExpressionsTest() {
        equal("4+6-98.2", 4+6-98.2);
        equal("(4+6-98.2)+4", (4+6-98.2)+4);
        equal("-(2-4)", -(2-4));
        equal("-(2-4)*(4+6-98.2)+4", -(2-4)*(4+6-98.2)+4);
        equal("23+4/5", 23+4d/5);
        equal("28/23.8", 28/23.8d);
        equal("23+4/5", 23+4d/5);
        equal("28+199/5", 28+199/5d);
        equal("(32-4)/(23+4/5)", (32-4)/(23+4/5d));
        equal("2-(32-4)/(23+4/5)", 2-(32d-4)/(23+4d/5));

        equal("2-(32-4)/(23+4/5)-(2-4)*(4+6-98.2)+4", 2-(32d-4)/(23+4d/5)-(2-4)*(4+6-98.2)+4);
    }

    @Test
    void aliasOperatorsTest() {
        equal("2*2", 2*2);
        //TODO: when pow is implemented equal("2**3", 2*2*2);
        equal("2*(3+1)", 2*(3+1));
        equal("2(3+1)", 2*(3+1));
    }

    @Test
    void multipleOperatorsTest() {
        equal("2++2", 2+2);
        equal("2++(3+1)", 2+3+1);
        equal("2-+2", 0);
        equal("-2+-3", -5);
    }
}
