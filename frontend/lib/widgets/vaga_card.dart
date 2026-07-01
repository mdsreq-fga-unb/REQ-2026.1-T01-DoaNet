import 'package:flutter/material.dart';

class VagaCard extends StatelessWidget {
  final String titulo;
  final String subtitulo;

  const VagaCard({
    super.key,
    required this.titulo,
    required this.subtitulo,
  });

  // Função que constrói e exibe o Pop-up na tela
  void _abrirPopupInscricao(BuildContext context) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return Dialog(
          backgroundColor: Colors.white,
          surfaceTintColor: Colors.transparent, // Mantém o fundo branco puro
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(24),
          ),
          insetPadding: const EdgeInsets.all(20), // Desgruda o popup das bordas da tela
          child: Padding(
            padding: const EdgeInsets.all(20.0),
            child: Column(
              mainAxisSize: MainAxisSize.min, // Faz o popup crescer só o necessário
              children: [
                // 1. Cabeçalho (Seta e Título)
                Row(
                  children: [
                    IconButton(
                      icon: const Icon(Icons.arrow_back, color: Colors.black),
                      onPressed: () => Navigator.of(context).pop(), // Fecha o popup
                    ),
                    const Expanded(
                      child: Center(
                        child: Text(
                          'Apoiar Projeto',
                          style: TextStyle(
                            fontSize: 24,
                            color: Colors.black,
                            fontWeight: FontWeight.w600,
                          ),
                        ),
                      ),
                    ),
                    const SizedBox(width: 48), // Espaço para manter o título centralizado
                  ],
                ),
                const SizedBox(height: 16),
                
                // 2. Linha divisória
                const Divider(color: Color(0xFFD9D9D9), thickness: 1),
                const SizedBox(height: 16),

                // 3. Card interno com as informações (Borda cinza)
                Container(
                  width: double.infinity,
                  padding: const EdgeInsets.all(20),
                  decoration: BoxDecoration(
                    borderRadius: BorderRadius.circular(16),
                    border: Border.all(color: const Color(0xFFD9D9D9), width: 1),
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Center(
                        child: Text(
                          titulo, // Puxa o título da vaga clicada
                          style: const TextStyle(
                            fontSize: 18,
                            fontWeight: FontWeight.bold,
                            color: Colors.black,
                          ),
                        ),
                      ),
                      const SizedBox(height: 16),
                      Text(
                        subtitulo, // Puxa o subtítulo da vaga clicada
                        style: const TextStyle(
                          fontSize: 14,
                          color: Color(0xFF505050),
                        ),
                      ),
                      const SizedBox(height: 16),
                      const Text(
                        'Como você vai ajudar:\nApoio escolar para alunos do 5º ao 9º', 
                        style: TextStyle(
                          fontSize: 14,
                          fontWeight: FontWeight.bold,
                          color: Colors.black,
                        ),
                      ),
                      const SizedBox(height: 16),
                      const Text(
                        'Local: Sede Principal, Asa Norte', 
                        style: TextStyle(
                          fontSize: 14,
                          fontWeight: FontWeight.bold,
                          color: Colors.black,
                        ),
                      ),
                    ],
                  ),
                ),
                const SizedBox(height: 24),

                // 4. Botão Verde de Inscrição
                SizedBox(
                  width: double.infinity,
                  height: 48,
                  child: ElevatedButton(
                    onPressed: () {
                      // A integração com a API virá aqui depois!
                      Navigator.of(context).pop(); // Fecha o popup simulando sucesso
                    },
                    style: ElevatedButton.styleFrom(
                      backgroundColor: const Color(0xFF1C824C), // Verde do botão
                      foregroundColor: Colors.white,
                      elevation: 0,
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(24),
                      ),
                    ),
                    child: const Text(
                      'Inscrever-se',
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
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: const EdgeInsets.only(bottom: 16),
      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 16),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(20),
        border: Border.all(
          color: const Color(0xFFD9D9D9),
          width: 1.5,
        ),
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  titulo,
                  style: const TextStyle(
                    fontSize: 16,
                    fontWeight: FontWeight.bold,
                    color: Color(0xFF171616),
                  ),
                ),
                const SizedBox(height: 4),
                Text(
                  subtitulo,
                  style: const TextStyle(
                    fontSize: 12,
                    color: Color(0xFF505050),
                  ),
                ),
              ],
            ),
          ),
          const SizedBox(width: 12),
          
          ElevatedButton(
            // Aqui é onde o botão chama o Pop-up ao ser clicado!
            onPressed: () => _abrirPopupInscricao(context), 
            style: ElevatedButton.styleFrom(
              backgroundColor: const Color(0xFF1C824C),
              foregroundColor: Colors.white,
              elevation: 0,
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(20),
              ),
              padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 10),
            ),
            child: const Text(
              'Inscrever',
              style: TextStyle(
                fontWeight: FontWeight.bold,
                fontSize: 14,
              ),
            ),
          ),
        ],
      ),
    );
  }
}