import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart'; 
import '../config/org_config_provider.dart';
import '../widgets/vaga_card.dart';
import '../info_fetch/oportunidades/fetch_oportunidade.dart';
import '../info_fetch/oportunidades/oportunidade_model.dart';

class ColaboracaoPage extends StatelessWidget {
  const ColaboracaoPage({super.key});

  @override
  Widget build(BuildContext context) {
    final config = OrgConfigProvider.of(context);

    return Container(
      child: ListView(
        padding: const EdgeInsets.symmetric(vertical: 16.0), 
        children: [
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
                      color: config.primaryColor, 
                      borderRadius: BorderRadius.circular(25),
                    ),
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
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

                // Substituímos a lista mocada pela conexão com o Banco
                FutureBuilder<List<OportunidadeItem>>(
                  future: FetchOportunidade(
                    orgId: OrgConfigProvider.of(context).orgId,
                  ).fetchOportunidades(),
                  builder: (context, snapshot) {
                    if (snapshot.connectionState == ConnectionState.waiting) {
                      return Center(
                        child: Padding(
                          padding: EdgeInsets.all(20.0),
                          child: CircularProgressIndicator(color: config.primaryColor),
                        )
                      );
                    } else if (snapshot.hasError) {
                      return Center(
                        child: Text(
                          'Erro ao carregar vagas: ${snapshot.error}', 
                          style: const TextStyle(color: Colors.red)
                        )
                      );
                    } else if (!snapshot.hasData || snapshot.data!.isEmpty) {
                      return const Center(
                        child: Text('Nenhuma oportunidade ativa no momento.')
                      );
                    }

                    final vagasReais = snapshot.data!;
                    
                    return Column(
                      children: vagasReais.map((vaga) => VagaCard(
                        titulo: vaga.titulo,
                        subtitulo: vaga.horario, 
                      )).toList(),
                    );
                  },
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}