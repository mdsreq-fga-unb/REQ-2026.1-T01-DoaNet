import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:url_launcher/url_launcher.dart';
import '../utils/input_formatters.dart';
import '../info_fetch/doacao/doacao_model.dart';
import '../info_fetch/doacao/doacao_service.dart';
import '../info_fetch/oportunidades/fetch_oportunidade.dart';
import '../info_fetch/oportunidades/oportunidade_model.dart';

void mostrarDoacaoDialog(BuildContext context) {
  showDialog(
    context: context,
    builder: (_) => const _DoacaoDialog(),
  );
}

class _DoacaoDialog extends StatefulWidget {
  const _DoacaoDialog();

  @override
  State<_DoacaoDialog> createState() => _DoacaoDialogState();
}

class _DoacaoDialogState extends State<_DoacaoDialog> {
  final _formKey = GlobalKey<FormState>();
  final _valorController = TextEditingController();
  final _nomeDoadorController = TextEditingController();
  final _cpfController = TextEditingController();
  final _logradouroController = TextEditingController();
  final _complementoController = TextEditingController();
  final _cidadeController = TextEditingController();
  final _estadoController = TextEditingController();
  final _cepController = TextEditingController();
  final _paisController = TextEditingController();

  VisibilidadeDoacao _visibilidade = VisibilidadeDoacao.publica;
  DirecaoDoacao _direcao = DirecaoDoacao.instituicao;
  bool _isLoading = false;

  List<OportunidadeItem> _oportunidades = [];
  bool _loadingOportunidades = false;
  String? _erroOportunidades;
  OportunidadeItem? _oportunidadeSelecionada;

  static const _azul = Color(0xFF0088FF);
  static const _cinzaBorda = Color(0xFFD9D9D9);
  static const _textoPrincipal = Color(0xFF171616);
  static const _textoSecundario = Color(0xFF505050);

  @override
  void initState() {
    super.initState();
    _carregarOportunidades();
  }

  @override
  void dispose() {
    _valorController.dispose();
    _nomeDoadorController.dispose();
    _cpfController.dispose();
    _logradouroController.dispose();
    _complementoController.dispose();
    _cidadeController.dispose();
    _estadoController.dispose();
    _cepController.dispose();
    _paisController.dispose();
    super.dispose();
  }

  Future<void> _carregarOportunidades() async {
    setState(() {
      _loadingOportunidades = true;
      _erroOportunidades = null;
    });
    try {
      final lista = await FetchOportunidade().fetchOportunidades();
      if (mounted) {
        setState(() {
          _oportunidades = lista.where((o) => o.ativo).toList();
          _loadingOportunidades = false;
        });
      }
    } catch (_) {
      if (mounted) {
        setState(() {
          _erroOportunidades = 'Não foi possível carregar os projetos.';
          _loadingOportunidades = false;
        });
      }
    }
  }

  Future<void> _submeter() async {
    if (!_formKey.currentState!.validate()) return;

    setState(() => _isLoading = true);

    try {
      final doacao = DoacaoRequest(
        valor: double.parse(_valorController.text.replaceAll(',', '.')),
        visibilidade: _visibilidade,
        // Nome sempre enviado (para transparência), independente do anonimato
        nomeDoador: _nomeDoadorController.text.trim(),
        cpf: _cpfController.text.trim(),
        endereco: EnderecoDoacao(
          logradouro: _logradouroController.text.trim(),
          complemento: _complementoController.text.trim(),
          cidade: _cidadeController.text.trim(),
          estado: _estadoController.text.trim(),
          cep: _cepController.text.trim(),
          pais: _paisController.text.trim(),
        ),
        direcao: _direcao,
        nomeProjeto: _direcao == DirecaoDoacao.projeto
            ? _oportunidadeSelecionada?.titulo
            : null,
      );

      final checkoutUrl = await DoacaoService().criarCheckoutSession(doacao);
      final uri = Uri.parse(checkoutUrl);

      if (!mounted) return;
      Navigator.of(context).pop();

      if (await canLaunchUrl(uri)) {
        await launchUrl(uri, mode: LaunchMode.externalApplication);
      } else {
        throw Exception('Não foi possível abrir o link de pagamento.');
      }
    } catch (e) {
      if (!mounted) return;
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text('Erro: ${e.toString()}'),
          backgroundColor: Colors.red,
        ),
      );
    } finally {
      if (mounted) setState(() => _isLoading = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Dialog(
      backgroundColor: Colors.white,
      surfaceTintColor: Colors.transparent,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(24)),
      insetPadding: const EdgeInsets.all(20),
      child: Padding(
        padding: const EdgeInsets.all(20),
        child: Form(
          key: _formKey,
          child: SingleChildScrollView(
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                // ── Cabeçalho ─────────────────────────────────────────
                Row(
                  children: [
                    IconButton(
                      icon: const Icon(Icons.arrow_back, color: _textoPrincipal),
                      onPressed: () => Navigator.of(context).pop(),
                    ),
                    const Expanded(
                      child: Center(
                        child: Text(
                          'Fazer Doação',
                          style: TextStyle(
                            fontSize: 24,
                            fontWeight: FontWeight.w600,
                            color: _textoPrincipal,
                          ),
                        ),
                      ),
                    ),
                    const SizedBox(width: 48),
                  ],
                ),
                const SizedBox(height: 16),
                const Divider(color: _cinzaBorda, thickness: 1),
                const SizedBox(height: 20),

                // ── Conteúdo do formulário ─────────────────────────────
                Container(
                  width: double.infinity,
                  padding: const EdgeInsets.all(20),
                  decoration: BoxDecoration(
                    borderRadius: BorderRadius.circular(16),
                    border: Border.all(color: _cinzaBorda, width: 1),
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      // ── Valor ────────────────────────────────────────
                      const Text(
                        'Valor da doação',
                        style: TextStyle(
                          fontSize: 14,
                          fontWeight: FontWeight.w600,
                          color: _textoPrincipal,
                        ),
                      ),
                      const SizedBox(height: 8),
                      TextFormField(
                        controller: _valorController,
                        keyboardType: const TextInputType.numberWithOptions(
                            decimal: true),
                        inputFormatters: [
                          FilteringTextInputFormatter.allow(
                              RegExp(r'[0-9.,]')),
                        ],
                        decoration: InputDecoration(
                          prefixText: 'R\$ ',
                          hintText: '0,00',
                          hintStyle:
                              const TextStyle(color: _textoSecundario),
                          contentPadding: const EdgeInsets.symmetric(
                              horizontal: 16, vertical: 12),
                          border: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(12),
                            borderSide: const BorderSide(color: _cinzaBorda),
                          ),
                          enabledBorder: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(12),
                            borderSide: const BorderSide(color: _cinzaBorda),
                          ),
                          focusedBorder: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(12),
                            borderSide:
                                const BorderSide(color: _azul, width: 1.5),
                          ),
                          errorBorder: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(12),
                            borderSide: const BorderSide(color: Colors.red),
                          ),
                          focusedErrorBorder: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(12),
                            borderSide: const BorderSide(
                                color: Colors.red, width: 1.5),
                          ),
                        ),
                        validator: (v) {
                          if (v == null || v.trim().isEmpty) {
                            return 'Informe o valor';
                          }
                          final val =
                              double.tryParse(v.replaceAll(',', '.'));
                          if (val == null || val <= 0) {
                            return 'Valor inválido';
                          }
                          return null;
                        },
                      ),
                      const SizedBox(height: 20),

                      // ── Nome do doador (sempre visível) ───────────────
                      const Text(
                        'Seu nome',
                        style: TextStyle(
                          fontSize: 14,
                          fontWeight: FontWeight.w600,
                          color: _textoPrincipal,
                        ),
                      ),
                      const SizedBox(height: 8),
                      TextFormField(
                        controller: _nomeDoadorController,
                        textCapitalization: TextCapitalization.words,
                        decoration: _inputDecoration('Digite seu nome'),
                        validator: (v) {
                          if (v == null || v.trim().isEmpty) {
                            return 'Informe seu nome';
                          }
                          return null;
                        },
                      ),
                      const SizedBox(height: 6),
                      const Text(
                        'Usado no registro de transparência. Selecione "Anônima" abaixo para não exibir seu nome publicamente.',
                        style: TextStyle(
                          fontSize: 12,
                          color: _textoSecundario,
                        ),
                      ),
                      const SizedBox(height: 20),

                      // ── CPF ──────────────────────────────────────────
                      const Text(
                        'CPF',
                        style: TextStyle(
                          fontSize: 14,
                          fontWeight: FontWeight.w600,
                          color: _textoPrincipal,
                        ),
                      ),
                      const SizedBox(height: 8),
                      TextFormField(
                        controller: _cpfController,
                        keyboardType: TextInputType.number,
                        inputFormatters: [CpfInputFormatter()],
                        decoration: _inputDecoration('000.000.000-00'),
                        validator: (v) {
                          if (v == null || v.trim().isEmpty) {
                            return 'Informe o CPF';
                          }
                          final digits = v.replaceAll(RegExp(r'\D'), '');
                          if (digits.length != 11) {
                            return 'CPF incompleto';
                          }
                          return null;
                        },
                      ),
                      const SizedBox(height: 20),

                      // ── Endereço ─────────────────────────────────────
                      const Text(
                        'Endereço',
                        style: TextStyle(
                          fontSize: 16,
                          fontWeight: FontWeight.w600,
                          color: _textoPrincipal,
                        ),
                      ),
                      const SizedBox(height: 12),
                      TextFormField(
                        controller: _logradouroController,
                        textCapitalization: TextCapitalization.words,
                        decoration: _inputDecoration('Endereço (rua, número)'),
                        validator: (v) {
                          if (v == null || v.trim().isEmpty) {
                            return 'Informe o endereço';
                          }
                          return null;
                        },
                      ),
                      const SizedBox(height: 12),
                      TextFormField(
                        controller: _complementoController,
                        textCapitalization: TextCapitalization.words,
                        decoration:
                            _inputDecoration('Complemento (opcional)'),
                      ),
                      const SizedBox(height: 12),
                      Row(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Expanded(
                            child: TextFormField(
                              controller: _cidadeController,
                              textCapitalization: TextCapitalization.words,
                              decoration: _inputDecoration('Cidade'),
                              validator: (v) {
                                if (v == null || v.trim().isEmpty) {
                                  return 'Informe a cidade';
                                }
                                return null;
                              },
                            ),
                          ),
                          const SizedBox(width: 12),
                          Expanded(
                            child: TextFormField(
                              controller: _estadoController,
                              textCapitalization: TextCapitalization.words,
                              decoration: _inputDecoration('Estado / Região'),
                              validator: (v) {
                                if (v == null || v.trim().isEmpty) {
                                  return 'Informe o estado';
                                }
                                return null;
                              },
                            ),
                          ),
                        ],
                      ),
                      const SizedBox(height: 12),
                      Row(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Expanded(
                            child: TextFormField(
                              controller: _cepController,
                              keyboardType: TextInputType.number,
                              inputFormatters: [CepInputFormatter()],
                              decoration: _inputDecoration('00000-000'),
                              validator: (v) {
                                if (v == null || v.trim().isEmpty) {
                                  return 'Informe o CEP';
                                }
                                final digits = v.replaceAll(RegExp(r'\D'), '');
                                if (digits.length != 8) {
                                  return 'CEP incompleto';
                                }
                                return null;
                              },
                            ),
                          ),
                          const SizedBox(width: 12),
                          Expanded(
                            child: TextFormField(
                              controller: _paisController,
                              textCapitalization: TextCapitalization.words,
                              decoration: _inputDecoration('País'),
                              validator: (v) {
                                if (v == null || v.trim().isEmpty) {
                                  return 'Informe o país';
                                }
                                return null;
                              },
                            ),
                          ),
                        ],
                      ),
                      const SizedBox(height: 20),

                      // ── Visibilidade ─────────────────────────────────
                      const Text(
                        'Visibilidade',
                        style: TextStyle(
                          fontSize: 14,
                          fontWeight: FontWeight.w600,
                          color: _textoPrincipal,
                        ),
                      ),
                      const SizedBox(height: 8),
                      _SegmentedToggle(
                        opcaoA: 'Pública',
                        opcaoB: 'Anônima',
                        selecionadoA:
                            _visibilidade == VisibilidadeDoacao.publica,
                        onTapA: () => setState(
                            () => _visibilidade = VisibilidadeDoacao.publica),
                        onTapB: () => setState(
                            () => _visibilidade = VisibilidadeDoacao.anonima),
                      ),

                      const SizedBox(height: 20),

                      // ── Direcionamento ───────────────────────────────
                      const Text(
                        'Direcionamento',
                        style: TextStyle(
                          fontSize: 14,
                          fontWeight: FontWeight.w600,
                          color: _textoPrincipal,
                        ),
                      ),
                      const SizedBox(height: 8),
                      _SegmentedToggle(
                        opcaoA: 'Instituição',
                        opcaoB: 'Projeto',
                        selecionadoA:
                            _direcao == DirecaoDoacao.instituicao,
                        onTapA: () => setState(() {
                          _direcao = DirecaoDoacao.instituicao;
                          _oportunidadeSelecionada = null;
                        }),
                        onTapB: () => setState(
                            () => _direcao = DirecaoDoacao.projeto),
                      ),

                      // ── Descrição do direcionamento ──────────────────
                      const SizedBox(height: 8),
                      Text(
                        _direcao == DirecaoDoacao.instituicao
                            ? 'Sua doação apoiará a MoveEduca de forma geral.'
                            : 'Selecione o projeto que deseja apoiar.',
                        style: const TextStyle(
                          fontSize: 12,
                          color: _textoSecundario,
                        ),
                      ),

                      // ── Dropdown de projetos (condicional) ────────────
                      if (_direcao == DirecaoDoacao.projeto) ...[
                        const SizedBox(height: 16),
                        const Text(
                          'Projeto',
                          style: TextStyle(
                            fontSize: 14,
                            fontWeight: FontWeight.w600,
                            color: _textoPrincipal,
                          ),
                        ),
                        const SizedBox(height: 8),
                        _buildDropdownProjeto(),
                      ],
                    ],
                  ),
                ),
                const SizedBox(height: 24),

                // ── Botão de pagamento ─────────────────────────────────
                SizedBox(
                  width: double.infinity,
                  height: 52,
                  child: ElevatedButton(
                    onPressed: _isLoading ? null : _submeter,
                    style: ElevatedButton.styleFrom(
                      backgroundColor: _azul,
                      foregroundColor: Colors.white,
                      elevation: 0,
                      disabledBackgroundColor: _azul.withValues(alpha: 0.6),
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(24),
                      ),
                    ),
                    child: _isLoading
                        ? const SizedBox(
                            width: 22,
                            height: 22,
                            child: CircularProgressIndicator(
                              color: Colors.white,
                              strokeWidth: 2.5,
                            ),
                          )
                        : const Text(
                            'Ir para pagamento',
                            style: TextStyle(
                              fontSize: 16,
                              fontWeight: FontWeight.bold,
                            ),
                          ),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildDropdownProjeto() {
    if (_loadingOportunidades) {
      return const SizedBox(
        height: 48,
        child: Center(
          child: SizedBox(
            width: 20,
            height: 20,
            child: CircularProgressIndicator(
              strokeWidth: 2,
              color: _azul,
            ),
          ),
        ),
      );
    }

    if (_erroOportunidades != null) {
      return Row(
        children: [
          const Icon(Icons.error_outline, color: Colors.red, size: 16),
          const SizedBox(width: 8),
          Expanded(
            child: Text(
              _erroOportunidades!,
              style: const TextStyle(color: Colors.red, fontSize: 13),
            ),
          ),
          TextButton(
            onPressed: _carregarOportunidades,
            child: const Text('Tentar novamente'),
          ),
        ],
      );
    }

    if (_oportunidades.isEmpty) {
      return Container(
        height: 48,
        alignment: Alignment.centerLeft,
        padding: const EdgeInsets.symmetric(horizontal: 16),
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(12),
          border: Border.all(color: _cinzaBorda),
        ),
        child: const Text(
          'Nenhum projeto cadastrado.',
          style: TextStyle(color: _textoSecundario, fontSize: 14),
        ),
      );
    }

    return DropdownButtonFormField<OportunidadeItem>(
      initialValue: _oportunidadeSelecionada,
      isExpanded: true,
      hint: const Text(
        'Selecione um projeto',
        style: TextStyle(color: _textoSecundario, fontSize: 14),
      ),
      icon: const Icon(Icons.keyboard_arrow_down, color: _textoSecundario),
      decoration: InputDecoration(
        contentPadding:
            const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(12),
          borderSide: const BorderSide(color: _cinzaBorda),
        ),
        enabledBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(12),
          borderSide: const BorderSide(color: _cinzaBorda),
        ),
        focusedBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(12),
          borderSide: const BorderSide(color: _azul, width: 1.5),
        ),
        errorBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(12),
          borderSide: const BorderSide(color: Colors.red),
        ),
        focusedErrorBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(12),
          borderSide: const BorderSide(color: Colors.red, width: 1.5),
        ),
      ),
      items: _oportunidades
          .map(
            (o) => DropdownMenuItem<OportunidadeItem>(
              value: o,
              child: Text(
                '${o.titulo}  •  ${o.horario}',
                overflow: TextOverflow.ellipsis,
                style: const TextStyle(
                  fontSize: 14,
                  color: _textoPrincipal,
                ),
              ),
            ),
          )
          .toList(),
      onChanged: (val) => setState(() => _oportunidadeSelecionada = val),
      validator: (_) {
        if (_direcao == DirecaoDoacao.projeto &&
            _oportunidadeSelecionada == null) {
          return 'Selecione um projeto';
        }
        return null;
      },
    );
  }

  InputDecoration _inputDecoration(String hint) {
    return InputDecoration(
      hintText: hint,
      hintStyle: const TextStyle(color: _textoSecundario),
      contentPadding:
          const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
      border: OutlineInputBorder(
        borderRadius: BorderRadius.circular(12),
        borderSide: const BorderSide(color: _cinzaBorda),
      ),
      enabledBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(12),
        borderSide: const BorderSide(color: _cinzaBorda),
      ),
      focusedBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(12),
        borderSide: const BorderSide(color: _azul, width: 1.5),
      ),
      errorBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(12),
        borderSide: const BorderSide(color: Colors.red),
      ),
      focusedErrorBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(12),
        borderSide: const BorderSide(color: Colors.red, width: 1.5),
      ),
    );
  }
}

// Toggle segmentado igual ao "Normal / Evento" do protótipo
class _SegmentedToggle extends StatelessWidget {
  final String opcaoA;
  final String opcaoB;
  final bool selecionadoA;
  final VoidCallback onTapA;
  final VoidCallback onTapB;

  const _SegmentedToggle({
    required this.opcaoA,
    required this.opcaoB,
    required this.selecionadoA,
    required this.onTapA,
    required this.onTapB,
  });

  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        Expanded(child: _Opcao(opcaoA, selecionadoA, onTapA)),
        const SizedBox(width: 8),
        Expanded(child: _Opcao(opcaoB, !selecionadoA, onTapB)),
      ],
    );
  }
}

class _Opcao extends StatelessWidget {
  final String label;
  final bool selecionada;
  final VoidCallback onTap;

  const _Opcao(this.label, this.selecionada, this.onTap);

  static const _azul = Color(0xFF0088FF);
  static const _cinzaBorda = Color(0xFFD9D9D9);

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: onTap,
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 200),
        height: 40,
        decoration: BoxDecoration(
          color: selecionada ? _azul : Colors.white,
          borderRadius: BorderRadius.circular(20),
          border: Border.all(
            color: selecionada ? _azul : _cinzaBorda,
            width: 1.5,
          ),
        ),
        alignment: Alignment.center,
        child: Text(
          label,
          style: TextStyle(
            fontSize: 14,
            fontWeight: FontWeight.w600,
            color: selecionada ? Colors.white : const Color(0xFF505050),
          ),
        ),
      ),
    );
  }
}
