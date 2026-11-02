using ASoftwareVersaoFisioterapiaAPI.Context;
using ASoftwareVersaoFisioterapiaAPI.Model;

namespace ASoftwareVersaoFisioterapiaAPI.Services.TimeControl
{
    public class TimeControlService : ITimeControlService
    {
        private readonly ASoftwareVersaoFisioterapiaAPIContext _context;

        public TimeControlService(ASoftwareVersaoFisioterapiaAPIContext context)
        {
            _context = context;
        }

        public DateTime Dateformat()
        {
            return DateTime.Now;
        }

        public bool ValidateTimeControl(DateTime dateTime)
        {
            try
            {
                return !_context.Clientes.Any((Cliente cliente) => cliente.DataDaConsulta == dateTime);
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.ToString());
                throw;
            }
        }
    }
}