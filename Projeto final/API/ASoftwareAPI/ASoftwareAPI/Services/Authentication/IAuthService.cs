namespace ASoftwareVersaoFisioterapiaAPI.Services.Authentication
{
    public interface IAuthService
    {
        bool ValidateUserAsync(string login, string senha);
    }
}