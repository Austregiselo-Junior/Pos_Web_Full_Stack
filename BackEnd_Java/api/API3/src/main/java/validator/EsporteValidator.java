package validator;


import jakarta.validation.ConstraintValidator;
import jakarta.validation.ConstraintValidatorContext;


public class EsporteValidator implements
        ConstraintValidator<EsporteValidation, String> {
    private String message;
    @Override
    public void initialize(EsporteValidation constraintAnnotation) {
        message = constraintAnnotation.message();
    }


    @Override
    public boolean isValid(String nome, ConstraintValidatorContext constraintValidatorContext) {
        if(!nome.contains("Futebol") && !nome.contains("Balet")) {
            return false;
        }
        constraintValidatorContext.disableDefaultConstraintViolation();
        constraintValidatorContext
                .buildConstraintViolationWithTemplate(message + nome)//
                .addConstraintViolation();
        return true;
    }

}
