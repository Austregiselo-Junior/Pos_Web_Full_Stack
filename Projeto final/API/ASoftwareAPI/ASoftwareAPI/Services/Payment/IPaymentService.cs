namespace ASoftwareVersaoFisioterapiaAPI.Services.Payment
{
    public interface IPaymentService
    {
        float TotalValue(float value, int numberOfSessions);

        float Payment(string type, float value, float discountPercentage, int numberOfSessions);
    }
}