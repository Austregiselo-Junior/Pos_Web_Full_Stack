using ASoftwareVersaoFisioterapiaAPI.Context;
using ASoftwareVersaoFisioterapiaAPI.Services.Authentication;
using Moq;

namespace APITest.Services.Authentication
{
    public class AuthServiceTests : IDisposable
    {
        private MockRepository mockRepository;

        private Mock<ASoftwareVersaoFisioterapiaAPIContext> mockASoftwareVersaoFisioterapiaAPIContext;

        public AuthServiceTests()
        {
            this.mockRepository = new MockRepository(MockBehavior.Strict);

            this.mockASoftwareVersaoFisioterapiaAPIContext = this.mockRepository.Create<ASoftwareVersaoFisioterapiaAPIContext>();
        }

        private AuthService CreateService()
        {
            return new AuthService(
                this.mockASoftwareVersaoFisioterapiaAPIContext.Object);
        }

        [Theory(DisplayName = "GIVEN authetication" +
            "WHEN user method validate is called" +
            "THEN the result is true")]
        [InlineData("adm", "adm")]
        public void ValidateUserAsync_StateUnderTest_ExpectedBehavior(string login, string loginFromDB)
        {
            // Arrange
            var service = this.CreateService();

            // Act
            var result = service.ValidateUserAsync(login, loginFromDB);

            // Assert
            result.Equals(true);
        }

        protected virtual void Dispose(bool disposing)
        {
            mockRepository.VerifyAll();
        }

        public void Dispose()
        {
            this.Dispose(true);
            GC.SuppressFinalize(this);
        }
    }
}