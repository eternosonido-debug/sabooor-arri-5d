# Validação da primeira versão 5D3

Código 2f52a7170404ef09060ba015cf82b799d3ab4a8a. Compilação e testes feitos no computador; nenhuma câmera ou cartão foi modificado. Pacotes experimentais para colaboradores com ML já funcional.

A base 5D3.113 compilou antes da ativação do tema. Depois do port, compilaram separadamente 5D3.113 e 5D3.123; a regressão 600D.102 também compilou dentro do seu limite específico. Não há teste físico de inicialização, gravação, áudio, HDMI, temperatura ou desempenho LUT.

Testes de código C: navegação da árvore de 319 nós, seletores e cancelamento, rótulos/modelo/sensor, overlay exclusivo e liberação de semáforo, moldura, falha de fontes, gates de LiveView/REC/HDMI, processamento dos três LUTs, checksum, limites de buffer e arquivos ausentes/corrompidos. Na 5D3 foi verificado que os itens de vídeo abrem o menu Canon sem escrever PROP_VIDEO_MODE/PROP_VIDEO_SYSTEM. Os testes dos controles da 600D permanecem separados.

O patch foi aplicado a uma cópia limpa do upstream fixado e todos os arquivos alterados foram comparados byte a byte com o código do build. Isso valida a reconstrução do código, não o funcionamento físico do equipamento.

A 5D3 usa a reserva dinâmica original boot-d45. Não se aplicou a ela o limite de memória fixo da 600D. O JSON registra os tamanhos estáticos; não há alegação de espaço de heap validado em hardware. Warnings de segmento RWX do linker correspondem ao formato de build upstream.

A Canon documenta 1080p 23,976/25/29,97, 720p 50/59,94 e VGA 50/59,94 para a 5D3; não se copiou a tabela VGA da 600D. Configuração de modo e ALL-I/IPB permanece nativa. Fontes: https://asia.canon/en/support/6200124200 e https://www.cla.canon.com/en/p/eos-5d-mark-iii ; restrição de troca em LiveView: upstream src/fps-engio.c, flip_zoom_twostage, CONFIG_DIGIC_V.
