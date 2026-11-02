namespace ASoftwareVersaoFisioterapiaAPI.Services.TimeControl
{
    public interface ITimeControlService
    {
        bool ValidateTimeControl(DateTime dateTime);

        DateTime Dateformat();
    }
}