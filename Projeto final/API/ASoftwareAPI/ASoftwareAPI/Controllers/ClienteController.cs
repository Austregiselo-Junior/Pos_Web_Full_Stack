using ASoftwareVersaoFisioterapiaAPI.Context;
using ASoftwareVersaoFisioterapiaAPI.Model;
using ASoftwareVersaoFisioterapiaAPI.Services.Payment;
using ASoftwareVersaoFisioterapiaAPI.Services.TimeControl;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace ASoftwareVersaoFisioterapiaAPI.Controllers
{
    [Route("[controller]")]
    [ApiController]
    public class ClienteController : ControllerBase
    {
        private readonly ASoftwareVersaoFisioterapiaAPIContext _context;
        private readonly ITimeControlService _timeControlService;
        private readonly IPaymentService _paymentControlService;

        public ClienteController(ASoftwareVersaoFisioterapiaAPIContext context, ITimeControlService timeControlService, IPaymentService paymentControlService)
        {
            _context = context;
            _timeControlService = timeControlService;
            _paymentControlService = paymentControlService;
        }

        #region Gets

        [HttpGet("TabelaSimples")]
        public ActionResult<IEnumerable<object>> GetTime()
        {
            var cliente = _context.Clientes.AsNoTracking().Select(c => new { c.Nome, c.Telefone, c.DataDaConsulta }).ToList();

            return (cliente is null) ? NotFound(new { message = "Cliente não encontrado." }) : Ok(cliente);
        }

        [HttpGet("TabelaDetalhada")]
        public ActionResult<IEnumerable<object>> GetAll()
        {
            try
            {
                var clientes = _context.Clientes.AsNoTracking().Select(c => new
                {
                    c.ClienteId,
                    c.Nome,
                    c.Telefone,
                    c.DataDaConsulta,
                    c.Categoria,
                    c.ValorDaSessao,
                    c.QuantidadeDeSessao,
                    c.ValorTotal,
                    c.Desconto,
                    c.ValorPago,
                    c.Vencimento,
                    c.SituacaoFinanceira,
                    c.DataDoCadastro
                }).ToList();

                return (clientes is null) ? StatusCode(500) : Ok(clientes);
            }
            catch (Exception ex)
            {
                return BadRequest(new { message = ex.Message });
            }
        }

        [HttpGet("{id:int}", Name = "ObterCliente")]
        public ActionResult<object> GetById(int id)
        {
            var cliente = _context.Clientes.AsNoTracking().Where(c => c.ClienteId == id).Select(c => new
            {
                c.Nome,
                c.Telefone,
                c.DataDaConsulta,
                c.Categoria,
                c.ValorDaSessao,
                c.QuantidadeDeSessao,
                c.ValorTotal,
                c.Desconto,
                c.ValorPago,
                c.Vencimento,
                c.SituacaoFinanceira
            }).FirstOrDefault();

            return (cliente is null) ? NotFound(new { message = "Cliente não encontrado." }) : Ok(cliente);
        }

        #endregion Gets

        [HttpPost("AdicionarCliente")]
        public ActionResult Post(Cliente cliente)
        {
            try
            {
                if (cliente == null)
                    return BadRequest();

                if (_timeControlService.ValidateTimeControl(cliente.DataDaConsulta))
                {
                    cliente.ValorTotal = _paymentControlService.TotalValue(cliente.ValorDaSessao, cliente.QuantidadeDeSessao);
                    cliente.ValorPago = _paymentControlService.Payment(cliente.Categoria, cliente.ValorDaSessao, cliente.Desconto, cliente.QuantidadeDeSessao);

                    cliente.UltimaAtualizacao = _timeControlService.Dateformat();

                    _context.Clientes.Add(cliente);
                    _context.SaveChanges();
                }
                else
                {
                    return BadRequest(new { message = "Error message: Horário não disponível!" });
                }

                return new CreatedAtRouteResult("ObterCliente", new { id = cliente.ClienteId }, Ok(cliente));
            }
            catch (Exception ex)
            {
                return BadRequest(new
                {
                    message = $"Error message: {ex.Message}," +
                    $" Inner exeption: {ex.InnerException}"
                });
            }
        }

        [HttpPut("AtualizarCliente")]
        public ActionResult Put(int id, Cliente cliente)
        {
            try
            {
                var hasclienteFromDB = _context?.Clientes.FirstOrDefault(c => c.ClienteId == id);

                if (hasclienteFromDB == null)
                    return BadRequest(new { message = "Cliente não encontrado" });

                cliente.ValorTotal = _paymentControlService.TotalValue(cliente.ValorDaSessao, cliente.QuantidadeDeSessao);
                cliente.ValorPago = _paymentControlService.Payment(cliente.Categoria, cliente.ValorDaSessao, cliente.Desconto, cliente.QuantidadeDeSessao);

                cliente.UltimaAtualizacao = _timeControlService.Dateformat();

                _context.Entry(hasclienteFromDB).State = EntityState.Detached;
                _context.Entry(cliente).State = Microsoft.EntityFrameworkCore.EntityState.Modified;
                _context.SaveChangesAsync();
                return Ok(cliente);
            }
            catch (Exception ex)
            {
                return BadRequest(new { message = $"Error message: {ex.Message}" });
            }
        }

        [HttpPut("AtualizarClienteDataConsulta")]
        public ActionResult PutDataDaConsulta(int id, Cliente cliente)
        {
            try
            {
                var hasclienteFromDB = _context?.Clientes.FirstOrDefault(c => c.ClienteId == id);

                if (hasclienteFromDB == null)
                    return BadRequest(new { message = "Cliente não encontrado" });

                if (_timeControlService.ValidateTimeControl(cliente.DataDaConsulta))
                {
                    return BadRequest(new { message = "Error message: Horário não disponível!" });
                }

                cliente.ValorTotal = _paymentControlService.TotalValue(cliente.ValorDaSessao, cliente.QuantidadeDeSessao);
                cliente.ValorPago = _paymentControlService.Payment(cliente.Categoria, cliente.ValorDaSessao, cliente.Desconto, cliente.QuantidadeDeSessao);

                cliente.UltimaAtualizacao = _timeControlService.Dateformat();

                _context.Entry(hasclienteFromDB).State = EntityState.Detached;
                _context.Entry(cliente).State = Microsoft.EntityFrameworkCore.EntityState.Modified;
                _context.SaveChangesAsync();
                return Ok(cliente);
            }
            catch (Exception ex)
            {
                return BadRequest(new { message = $"Error message: {ex.Message}" });
            }
        }

        [HttpDelete("RemoverCliente")]
        public ActionResult Delete(int id)
        {
            var clienteFromDB = _context?.Clientes.FirstOrDefault((Cliente c) => c.ClienteId == id);

            if (clienteFromDB == null)
                return NotFound(new { message = "Cliente não encontrado" });

            _context?.Clientes.Remove(clienteFromDB);
            _context?.SaveChanges();
            return Ok(clienteFromDB);
        }
    }
}