import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart'; 
import '../widgets/vaga_card.dart';

class ColaboracaoPage extends StatelessWidget {
  const ColaboracaoPage({super.key});

  @override
  Widget build(BuildContext context) {
    
    final List<Map<String, String>> vagasMocadas = [
      {'titulo': 'Professor de Reforço', 'subtitulo': 'Sábado, 14h as 16h'},
      {'titulo': 'Organizador de Eventos', 'subtitulo': 'Flexível'},
      {'titulo': 'Designer Gráfico', 'subtitulo': 'Remoto'},
      {'titulo': 'Mentoria de Carreira', 'subtitulo': 'Terça, 19h as 20h'},
      {'titulo': 'Apoio Psicológico', 'subtitulo': 'Quarta, 18h as 20h'},
      {'titulo': 'Desenvolvedor Web', 'subtitulo': 'Remoto'},
      {'titulo': 'Fotógrafo Voluntário', 'subtitulo': 'Sábado, 09h as 12h'},
      {'titulo': 'Coordenador de Doações', 'subtitulo': 'Flexível'},
    ];

    return Container(
      color: Colors.white,
      child: ListView(
        // Tirei o padding horizontal daqui!
        padding: const EdgeInsets.symmetric(vertical: 16.0), 
        children: [
          // Título com Padding para não encostar na borda
          const Padding(
            padding: EdgeInsets.symmetric(horizontal: 24.0),
            child: Center(
              child: Text(
                'Colaboração',
                style: TextStyle(
                  fontFamily: 'Roboto',
                  fontSize: 26,
                  fontWeight: FontWeight.w600,
                  color: Color(0xFF171616),
                ),
              ),
            ),
          ),
          const SizedBox(height: 16),
          
          const Divider(color: Color(0xFFD9D9D9), thickness: 1),
          const SizedBox(height: 24),

          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 24.0),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                InkWell(
                  onTap: () {},
                  borderRadius: BorderRadius.circular(25),
                  child: Container(
                    width: double.infinity, 
                    height: 165, 
                    decoration: BoxDecoration(
                      color: const Color(0xFF0088FF), 
                      borderRadius: BorderRadius.circular(25),
                    ),
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        // O seu SVG aqui
                        SvgPicture.asset(
                          'assets/icons/doacao.svg', 
                          height: 80, 
                          colorFilter: const ColorFilter.mode(Colors.white, BlendMode.srcIn)
                        ),
                        const SizedBox(width: 16),
                        const Text(
                          'Fazer Doação',
                          style: TextStyle(
                            fontFamily: 'Inter',
                            fontSize: 32, 
                            fontWeight: FontWeight.w600,
                            color: Colors.white,
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
                const SizedBox(height: 32),

                const Text(
                  'Ser Voluntariado',
                  style: TextStyle(
                    fontSize: 22,
                    fontWeight: FontWeight.bold,
                    color: Color(0xFF171616),
                  ),
                ),
                const SizedBox(height: 16),

                ...vagasMocadas.map((vaga) => VagaCard(
                  titulo: vaga['titulo']!,
                  subtitulo: vaga['subtitulo']!,
                )),
              ],
            ),
          ),
        ],
      ),
    );
  }
}