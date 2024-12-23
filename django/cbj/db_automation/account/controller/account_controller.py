from django.http import JsonResponse
from rest_framework import viewsets, status

from account.service.account_service_impl import AccountServiceImpl


class AccountController(viewsets.ViewSet):
    __accountService = AccountServiceImpl.getInstance()

    def requestCreateCarRegistrationData(self, request):
        isSuccess = self.__accountService.createAccount()

        return JsonResponse({'success': isSuccess})
