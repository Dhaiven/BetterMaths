package org.bettermaths.set.operation;

import org.bettermaths.result.Result;
import org.bettermaths.set.Set;

import java.util.ArrayList;
import java.util.List;

public class IntersectionSet implements Set {

    protected final List<Set> intersectionSets = new ArrayList<>();

    public IntersectionSet(Set first, Set second) {
        this.intersectionSets.add(first);
        this.intersectionSets.add(second);
    }

    public IntersectionSet(List<Set> intersectionSet) {
        this.intersectionSets.addAll(intersectionSet);
    }

    @Override
    public boolean contains(Set other) {
        for (Set intersectionSet : intersectionSets) {
            if (!intersectionSet.contains(other)) {
                return false;
            }
        }

        return true;
    }

    @Override
    public boolean strictContains(Set other) {
        for (Set intersectionSet : intersectionSets) {
            if (!intersectionSet.strictContains(other)) {
                return false;
            }
        }

        return true;
    }

    @Override
    public boolean belongs(Result<?> other) {
        for (Set intersectionSet : intersectionSets) {
            if (!intersectionSet.belongs(other)) {
                return false;
            }
        }

        return true;
    }
}
