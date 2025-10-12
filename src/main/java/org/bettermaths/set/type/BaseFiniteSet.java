package org.bettermaths.set.type;

import org.bettermaths.result.Result;
import org.bettermaths.result.custom.UpletResult;
import org.bettermaths.set.FiniteSet;
import org.bettermaths.set.Set;

import java.util.Collection;
import java.util.HashSet;

public class BaseFiniteSet implements FiniteSet {

    private final java.util.Set<Result<?>> elements = new HashSet<>();

    public BaseFiniteSet(Collection<Result<?>> elements) {
        this.elements.addAll(elements);
    }

    public java.util.Set<Result<?>> getElements() {
        return elements;
    }

    public boolean contains(Set other) {
        for (Result<?> element : elements) {
            if (!other.belongs(element)) {
                return false;
            }
        }

        return true;
    }

    public boolean strictContains(Set other) {
        return !equals(other) && contains(other);
    }

    public boolean belongs(Result<?> other) {
        return elements.contains(other);
    }

    public int cardinality() {
        return elements.size();
    }

    public FiniteSet cartesianProduct(FiniteSet other) {
        HashSet<Result<?>> values = new HashSet<>();
        for (var element : elements) {
            for (var otherElement : other.getElements()) {
                values.add(new UpletResult(element, otherElement));
            }
        }

        return new BaseFiniteSet(values);
    }
}
