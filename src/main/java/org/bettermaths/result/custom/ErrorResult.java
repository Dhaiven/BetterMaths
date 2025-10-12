package org.bettermaths.result.custom;

import org.bettermaths.result.Result;

public class ErrorResult implements Result<Object> {

    public static final ErrorResult ERROR = new ErrorResult();

    private ErrorResult() {}

    @Override
    public Object get() {
        return null;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        return obj instanceof ErrorResult;
    }

    @Override
    public int hashCode() {
        return ErrorResult.class.hashCode();
    }
}
