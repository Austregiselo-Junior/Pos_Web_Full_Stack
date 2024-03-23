package com.kamikase.web.posbackend.validator;

import jakarta.validation.Constraint;
import jakarta.validation.Payload;

import java.lang.annotation.*;

@Target( { ElementType.FIELD, ElementType.PARAMETER })
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Constraint(validatedBy = CustonValidator.class)
public @interface CustonValidation {
    String message() default "Clube inválido";
    Class<?>[] groups() default {};
    Class <?extends Payload>[] payload() default {};
}
