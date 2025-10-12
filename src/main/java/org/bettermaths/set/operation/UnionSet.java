package org.bettermaths.set.operation;

import org.bettermaths.result.Result;
import org.bettermaths.set.Set;

import java.util.ArrayList;
import java.util.List;

public class UnionSet implements Set {

    protected final List<Set> unionSets = new ArrayList<>();

    public UnionSet(Set first, Set second) {
        this.unionSets.add(first);
        this.unionSets.add(second);
    }

    public UnionSet(List<Set> unionSets) {
        this.unionSets.addAll(unionSets);
    }

    @Override
    public boolean contains(Set other) {
        for (Set unionSet : unionSets) {
            if (unionSet.contains(other)) {
                return true;
            }
        }

        return false;
    }

    @Override
    public boolean strictContains(Set other) {
        for (Set unionSet : unionSets) {
            if (unionSet.strictContains(other)) {
                return true;
            }
        }

        return false;
    }

    @Override
    public boolean belongs(Result<?> other) {
        for (Set unionSet : unionSets) {
            if (unionSet.belongs(other)) {
                return true;
            }
        }

        return false;
    }
}
