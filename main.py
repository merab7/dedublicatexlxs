from dedublicatorclass import ToyotaDeduplicator

#dedublicating SCION.xlsx
file_path = 'SCION.xlsx'
dedublicated_file_path = 'SCION_deduplicated_file.xlsx'

deduplicator = ToyotaDeduplicator(file_path)
deduplicator.read_data()
deduplicator.proces_data()
deduplicator.save_data(dedublicated_file_path)