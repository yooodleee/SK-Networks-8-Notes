import 'package:first/interview/domain/usecases/list/response/interview_list_response.dart';

abstract class ListInterviewUseCase {
  Future<InterviewListResponse> call(int page, int perPage, String userToken);
}