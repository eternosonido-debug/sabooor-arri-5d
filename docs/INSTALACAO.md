# Pacotes de desenvolvimento — 5D Mark III

Destinados a colaboradores que já tenham Magic Lantern funcionando no **mesmo firmware Canon do pacote**. 5D3.113 e 5D3.123 são alvos diferentes e não podem ser misturados. Não usar em outra 5D ou outro firmware; presença na matriz não significa suporte.

Os ZIPs de teste contêm somente o core, seus símbolos, fontes OFL e os três LUTs. Não contêm instalador FIR e não alteram bootflags. Nenhum cartão ou câmera foi modificado nesta etapa.

1. Salvar backup de autoexec.bin, símbolo ML/modules/5D3_113.sym ou 5D3_123.sym, fontes sabo12/sabo16b e configurações. Usar cartão separado, com o ML original do alvo já funcionando.
2. Conferir SHA256SUMS do pacote escolhido e preservar a estrutura ao copiar. Manter os módulos originais do mesmo build/alvo; módulos externos não foram auditados.
3. Ejetar com segurança e colocar na câmera desligada. No ML, Prefs > Sabooor ARRI > Monitor ou HOME. O padrão continua Original. INFO dentro do tema dá acesso à apresentação original.
4. Validar primeiro sem gravar, depois fazer um clipe curto e conferir o arquivo num computador. Registrar modelo/firmware, arquivo de log, passos e resultado. Validar CF e SD separadamente e depois HDMI.
5. Para voltar, restaurar juntos core, símbolo e fontes anteriores. O modo Original também desativa a apresentação do tema.

O teste no computador não confirma inicialização física, desempenho, temperatura, áudio, gravação, HDMI ou compatibilidade com todos os módulos. Look é prévia LCD; não é LUT de gravação. A troca de formato permanece no menu Canon. Não executar atualização/downgrade de firmware com base nestes pacotes.
