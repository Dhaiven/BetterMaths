package org.bettermaths.token.function;

import org.bettermaths.result.Result;

import java.util.ArrayList;
import java.util.List;

public class Params {

    private final ArrayList<Result<?>> param = new ArrayList<>();

    public List<Result<?>> values() {
        return param;
    }

    /**
     * Return all values that have the same type that {@code type}
     */
    public <T extends Result<?>> List<T> values(Class<T> type) {
        ArrayList<T> values = new ArrayList<>();
        for (Result<?> r : param) {
            if (type.isInstance(r)) {
                values.add(type.cast(r));
            }
        }

        return values;
    }

    public List<Result<?>> values(int start) {
        return values(start, param.size());
    }

    public List<Result<?>> values(int start, int end) {
        return param.subList(start, end);
    }

    public List<Result<?>> values(int start, int end, int step) {
        var subList = values(start, end);
        List<Result<?>> values = new ArrayList<>();
        for (int i = 0; i < subList.size(); i++) {
            if (i % step == 0) {
                values.add(subList.get(i));
            }
        }

        return values;
    }

    public <T extends Result<?>> List<Result<?>> values(Class<T> type, int start, int end) {
        List<Result<?>> values = new ArrayList<>();
        for (Result<?> r : values(start, end)) {
            if (type.isInstance(r)) {
                values.add(type.cast(r));
            }
        }

        return values;
    }

    public <T extends Result<?>> T get(int pos) {
        return (T) param.get(pos);
    }

    public void add(Result<?> r) {
        param.add(r);
    }

    public int size() {
        return param.size();
    }

    @Override
    public String toString() {
        return param.toString();
    }
}
