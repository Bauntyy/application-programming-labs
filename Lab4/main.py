from data_frame import create_dataframe, filter_dataframe, plot_area_distribution, add_area_column, add_hwd_columns
import parser


def main() -> None:
    arg=parser.parser()

    #Демонстрация работы
    df_images = create_dataframe(arg.csv_path)
    print("Source DataFrame:")
    print(df_images)

    print("DataBase with extra columns")
    df_images = add_hwd_columns(df_images)
    print(df_images)

    df_images = filter_dataframe(df_images, arg.max_height, arg.max_width)
    print("Filtered DataFrame:")
    print(df_images)

    filtered_df = add_area_column(df_images)
    sorted_df = filtered_df.sort_values(by='Area')
    print("Sorted DataFrame by area:")
    print(sorted_df)

    plot_area_distribution(sorted_df)

if __name__ == "__main__":
    main()