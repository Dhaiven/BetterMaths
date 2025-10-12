package org.bettermaths.set;

import org.bettermaths.result.Result;
import org.bettermaths.set.operation.ComplementarySet;
import org.bettermaths.set.operation.IntersectionSet;
import org.bettermaths.set.operation.UnionSet;

public interface Set {

    /**
     * A ⊆ B
     */
    boolean contains(Set other);

    /**
     * A ⊂ B
     */
    boolean strictContains(Set other);

    /**
     * x ∈ A
     */
    boolean belongs(Result<?> other);

    default ComplementarySet complementary() {
        return new ComplementarySet(this);
    }

    /**
     * AuB
     */
    default UnionSet union(Set other) {
        return new UnionSet(this, other);
    }

    /**
     * AnB
     */
    default IntersectionSet intersection(Set other) {
        return new IntersectionSet(this, other);
    }

    /**
     * A \ B = An  Bc
     */
    default IntersectionSet difference(Set other) {
        return new IntersectionSet(this, other.complementary());
    }

    default UnionSet symmetricDifference(Set other) {
        return new UnionSet(this.difference(other), other.difference(this));
    }
}
