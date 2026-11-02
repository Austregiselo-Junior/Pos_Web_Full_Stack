using ASoftwareVersaoFisioterapiaAPI.Context;

namespace ASoftwareVersaoFisioterapiaAPI.Services.Payment
{
    public class PaymentService : IPaymentService
    {
        private readonly ASoftwareVersaoFisioterapiaAPIContext _context;
        private const string _session = "Sessão";

        public PaymentService(ASoftwareVersaoFisioterapiaAPIContext context)
        {
            _context = context;
        }

        public float TotalValue(float value, int numberOfSessions)
        {
            return value * numberOfSessions;
        }

        private float TotalValueBySession(float value, float discountPercentage, int numberOfSessions)
        {
            if (value < 0 || numberOfSessions < 0 || discountPercentage < 0 || value == 0 || numberOfSessions == 0 || discountPercentage == 0)
            {
                return 0;
            }
            return TotalValue(value, numberOfSessions) - (value * numberOfSessions) * (discountPercentage / 100);
        }

        public bool IsCategoryBySerrion(string type)
        {
            return type.Equals(_session);
        }

        public float Payment(string type, float value, float discountPercentage, int numberOfSessions)
        {
            if (IsCategoryBySerrion(type) || discountPercentage == 0)
            {
                return TotalValue(value, numberOfSessions);
            }
            return TotalValueBySession(value, discountPercentage, numberOfSessions);
        }
    }
}