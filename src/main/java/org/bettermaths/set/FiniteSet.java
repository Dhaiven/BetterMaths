package org.bettermaths.set;

import org.bettermaths.result.Result;

public interface FiniteSet extends Set {

    java.util.Set<Result<?>> getElements();

}
